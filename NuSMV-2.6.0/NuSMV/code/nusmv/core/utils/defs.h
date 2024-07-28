/* ---------------------------------------------------------------------------


  This file is part of the ``utils'' package of NuSMV version 2.
  Copyright (C) 2007 by FBK-irst.

  NuSMV version 2 is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2 of the License, or (at your option) any later version.

  NuSMV version 2 is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.

  For more information on NuSMV see <http://nusmv.fbk.eu>
  or email to <nusmv-users@fbk.eu>.
  Please report bugs to <nusmv-users@fbk.eu>.

  To contact the NuSMV development board, email to <nusmv@fbk.eu>.

-----------------------------------------------------------------------------*/

/*!
  \author Roberto Cavada
  \brief Some low-level definitions

  Some low-level definitions

*/
#ifndef __DEFS_H__
#define __DEFS_H__

// Include the header where util_ptrint and util_ptruint are defined
#include "util.h"

// Define util_ptrint and util_ptruint if they are not defined in util.h
#ifndef util_ptrint
typedef intptr_t util_ptrint;
#endif

#ifndef util_ptruint
typedef uintptr_t util_ptruint;
#endif

typedef util_ptrint  nusmv_ptrint;
typedef util_ptruint nusmv_ptruint;

#ifndef __NUSMV_CORE_UTILS_DEFS_H__
#define __NUSMV_CORE_UTILS_DEFS_H__

#if HAVE_CONFIG_H
#  include "nusmv-config.h"
#endif

#if NUSMV_HAVE_STDLIB_H
#  include <stdlib.h>
#endif

#include <assert.h>
#include "cudd/util.h"

#  ifndef NUSMV_GCC_WARN_UNUSED_RESULT
#    define NUSMV_GCC_WARN_UNUSED_RESULT
#  endif

#ifdef EXTERN
# ifndef HAVE_EXTERN_ARGS_MACROS
    /* EXTERN is supposed to be no longer used if not explicitly required */
#   undef EXTERN
# endif
#endif

#ifdef ARGS
# ifndef HAVE_EXTERN_ARGS_MACROS
    /* ARGS is supposed to be no longer used if not explicitly required */
#   undef ARGS
# endif
#endif

/* These are potential duplicates. */
#if HAVE_EXTERN_ARGS_MACROS
# ifndef EXTERN
#   ifdef __cplusplus
#	define EXTERN extern "C"
#   else
#	define EXTERN extern
#   endif
# endif
# ifndef ARGS
#   if defined(__STDC__) || defined(__cplusplus) || defined(_MSC_VER)
#	define ARGS(protos)	protos		/* ANSI C */
#   else /* !(__STDC__ || __cplusplus || defined(_MSC_VER)) */
#	define ARGS(protos)	()		/* K&R C */
#   endif /* !(__STDC__ || __cplusplus || defined(_MSC_VER)) */
# endif
#endif

#ifndef NORETURN
#   if defined __GNUC__
#       define NORETURN __attribute__ ((__noreturn__))
#   else
#       define NORETURN
#   endif
#endif

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
#define nusmv_assert(expr) \
    assert(expr)

#if NUSMV_HAVE_RANDOM
#  define utils_random() \
    random()
#else
#  define utils_random() \
    rand()
#endif

#if NUSMV_HAVE_STDBOOL_H
#include <stdbool.h>

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
typedef bool boolean;
#else
#ifdef __cplusplus
typedef bool boolean;
#else
typedef enum {false=0, true=1} boolean;
#endif
#endif

/* MD If OUTCOME_SUCCESS would have the value 0 it would be consistent with
   the usual boolean representation */
typedef enum Outcome_TAG
{
  OUTCOME_GENERIC_ERROR,
  OUTCOME_PARSER_ERROR,
  OUTCOME_SYNTAX_ERROR,
  OUTCOME_FILE_ERROR,
  OUTCOME_SUCCESS_REQUIRED_HELP,
  OUTCOME_SUCCESS
} Outcome;

/* to avoid warnings */

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
#define UNUSED_PARAM(x) (void)(x)

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
#define UNUSED_VAR(x) (void)(x)

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
#define ENUM_CHECK(value, first, last) \
  nusmv_assert(first < value && value < last)

/* useful placeholders ********************************************************/
/*!
  \brief for switch cases without break
*/
#define FALLTHROUGH

/* for functions calling ErrorMgr_nusmv_exit or calling another function
   calling it and not catching it */

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
#define THROWS_EXCEPTION

/* for underling the use of comma operator */

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
#define COMMA_OPERATOR ,

 /* type for comparison function */

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
typedef int (*PFIVPVP)(const void*, const void*);

/* Generic void function */

/*!
  \brief \todo Missing synopsis

  \todo Missing description
*/
typedef void* (*PFVPVPVP)(void*, void*);

#endif /* __NUSMV_CORE_UTILS_DEFS_H__ */
#endif /* __DEFS_H__ */
