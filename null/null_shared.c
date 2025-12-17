/*
===========================================================================
Copyright (C) 2025 Alibek Omarov

This file is part of Quake III Arena source code.

Quake III Arena source code is free software; you can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.

Quake III Arena source code is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
===========================================================================
*/
#include "q_shared.h"
#include "qcommon.h"

char **Sys_ListFiles( const char *directory, const char *extension, char *filter, int *numfiles, qboolean wantsubs )
{
	return NULL;
}

void Sys_FreeFileList( char **list )
{
}

void Sys_ShowConsole( int visLevel, qboolean quitOnClose )
{
}

void Sys_SnapVector( float *v ) { // bk001213 - see win32/win_shared.c
  // bk001213 - old linux
  v[0] = rint(v[0]);
  v[1] = rint(v[1]);
  v[2] = rint(v[2]);
}

char *Sys_DefaultCDPath(void)
{
	static char null[1] = { 0 };
        return null;
}

char *Sys_DefaultInstallPath(void)
{
	static char null[1] = { 0 };
        return null;
}

char *Sys_DefaultHomePath(void)
{
	static char null[1] = { 0 };
        return null;
}
