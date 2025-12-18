#!/usr/bin/env python3
# encoding: utf-8
# Copyright 2025 Alibek Omarov
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from waflib import Build

class Subproject:
	def __init__(self, name, fnFilter = None):
		self.name = name
		self.fnFilter = fnFilter

	def is_exists(self, ctx):
		return ctx.path.find_node(self.name + '/wscript')

	def is_enabled(self, ctx):
		if not self.is_exists(ctx):
			return False

		if self.fnFilter:
			return self.fnFilter(ctx)

		return True

SUBDIRS = [
	Subproject("null"),
	Subproject("engine"),

	Subproject("cgame"),
	Subproject("game"),
	Subproject("ui"),
]

def options(opt):
	opt.load('reconfigure compiler_optimizations xcompile compiler_c sdl2 clang_compilation_database strip_on_install waf_unit_test msvs subproject')

	grp = opt.add_option_group('Common options')
	grp.add_option('--disable-rpath', action = 'store_false', dest = 'ENABLE_RPATH', default = True,
		help = 'disables rpath, duh!')


	for i in SUBDIRS:
		if not i.is_exists(opt):
			continue

		opt.add_subproject(i.name)

def configure(conf):
	conf.load('fwgslib reconfigure compiler_optimizations xcompile compiler_c msvs subproject clang_compilation_database strip_on_install waf_unit_test enforce_pic force_32bit')

	conf.check_pic(True)
	conf.force_32bit()

	cflags, linkflags = conf.get_optimization_flags()

	# because we're building everything in separate static libs, put this flag temporarily
	linkflags += ['-Wl,--no-as-needed']
	conf.env.append_unique('CFLAGS', cflags)
	conf.env.append_unique('LINKFLAGS', linkflags)

	conf.check_cc(cflags=cflags, linkflags=linkflags, msg='Checking for required C flags')

	conf.check_cc(lib='dl')
	conf.check_cc(lib='m')

	conf.check_large_file(compiler='c', execute=False)

	conf.env.SHAREDIR = conf.env.LIBDIR = conf.env.BINDIR = conf.env.PREFIX

	for i in SUBDIRS:
		if not i.is_enabled(conf):
			continue

		conf.add_subproject(i.name)

def build(bld):
	# don't clean QtCreator files and reconfigure saved options
	bld.clean_files = bld.bldnode.ant_glob('**',
		excl='*.user configuration.py .lock* *conf_check_*/** config.log 3rdparty/libbacktrace/*.h %s/*' % Build.CACHE_DIR,
		quiet=True, generator=True)

	for i in SUBDIRS:
		if not i.is_enabled(bld):
			continue

		bld.add_subproject(i.name)

