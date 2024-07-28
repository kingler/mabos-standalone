/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton implementation for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.3"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Using locations.  */
#define YYLSP_NEEDED 0

/* Substitute the variable and function names.  */
#define yyparse nusmv_yyparse
#define yylex   nusmv_yylex
#define yyerror nusmv_yyerror
#define yylval  nusmv_yylval
#define yychar  nusmv_yychar
#define yydebug nusmv_yydebug
#define yynerrs nusmv_yynerrs


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     TOK_ITYPE = 258,
     TOK_CONSTRAINT = 259,
     TOK_MAXU = 260,
     TOK_MINU = 261,
     TOK_ABU = 262,
     TOK_EBU = 263,
     TOK_AU = 264,
     TOK_EU = 265,
     TOK_CONTEXT = 266,
     TOK_PROCESS = 267,
     TOK_MODULE = 268,
     TOK_NAME = 269,
     TOK_COMPUTE = 270,
     TOK_LTLSPEC = 271,
     TOK_CTLSPEC = 272,
     TOK_SPEC = 273,
     TOK_INVAR = 274,
     TOK_TRANS = 275,
     TOK_INIT = 276,
     TOK_ARRAY_DEFINE = 277,
     TOK_DEFINE = 278,
     TOK_FUN = 279,
     TOK_IVAR = 280,
     TOK_FROZENVAR = 281,
     TOK_VAR = 282,
     TOK_PSLSPEC = 283,
     TOK_CONSTANTS = 284,
     TOK_JUSTICE = 285,
     TOK_COMPASSION = 286,
     TOK_FAIRNESS = 287,
     TOK_INVARSPEC = 288,
     TOK_ASSIGN = 289,
     TOK_ISA = 290,
     TOK_SEMI = 291,
     TOK_CONS = 292,
     TOK_OF = 293,
     TOK_RCB = 294,
     TOK_LCB = 295,
     TOK_RB = 296,
     TOK_RP = 297,
     TOK_LP = 298,
     TOK_TWODOTS = 299,
     TOK_EQDEF = 300,
     TOK_SELF = 301,
     TOK_COLON = 302,
     TOK_ESAC = 303,
     TOK_CASE = 304,
     TOK_COMPID = 305,
     TOK_COMPWFF = 306,
     TOK_CTLWFF = 307,
     TOK_LTLPSL = 308,
     TOK_LTLWFF = 309,
     TOK_NEXTWFF = 310,
     TOK_SIMPWFF = 311,
     TOK_INCONTEXT = 312,
     TOK_WORD = 313,
     TOK_BOOLEAN = 314,
     TOK_ARRAY = 315,
     TOK_WORD1 = 316,
     TOK_BOOL = 317,
     TOK_WAWRITE = 318,
     TOK_WAREAD = 319,
     TOK_CONST_ARRAY = 320,
     TOK_COUNT = 321,
     TOK_WTOINT = 322,
     TOK_WSIZEOF = 323,
     TOK_WRESIZE = 324,
     TOK_SWCONST = 325,
     TOK_UWCONST = 326,
     TOK_EXTEND = 327,
     TOK_UNSIGNED = 328,
     TOK_SIGNED = 329,
     TOK_TYPEOF = 330,
     TOK_TRUEEXP = 331,
     TOK_FALSEEXP = 332,
     TOK_ATOM = 333,
     TOK_NUMBER_EXP = 334,
     TOK_NUMBER_REAL = 335,
     TOK_NUMBER_FRAC = 336,
     TOK_NUMBER = 337,
     TOK_NUMBER_WORD = 338,
     TOK_MAX = 339,
     TOK_MIN = 340,
     TOK_ABS = 341,
     TOK_QUESTIONMARK = 342,
     TOK_NOT = 343,
     TOK_AND = 344,
     TOK_XNOR = 345,
     TOK_XOR = 346,
     TOK_OR = 347,
     TOK_IFF = 348,
     TOK_IMPLIES = 349,
     TOK_COMMA = 350,
     TOK_AA = 351,
     TOK_EE = 352,
     TOK_AG = 353,
     TOK_EG = 354,
     TOK_AF = 355,
     TOK_EF = 356,
     TOK_AX = 357,
     TOK_EX = 358,
     TOK_RELEASES = 359,
     TOK_TRIGGERED = 360,
     TOK_UNTIL = 361,
     TOK_SINCE = 362,
     TOK_MMAX = 363,
     TOK_MMIN = 364,
     TOK_BUNTIL = 365,
     TOK_ABG = 366,
     TOK_ABF = 367,
     TOK_EBG = 368,
     TOK_EBF = 369,
     TOK_OP_FUTURE = 370,
     TOK_OP_GLOBAL = 371,
     TOK_OP_NEXT = 372,
     TOK_OP_ONCE = 373,
     TOK_OP_HISTORICAL = 374,
     TOK_OP_NOTPRECNOT = 375,
     TOK_OP_PREC = 376,
     TOK_GE = 377,
     TOK_LE = 378,
     TOK_GT = 379,
     TOK_LT = 380,
     TOK_NOTEQUAL = 381,
     TOK_EQUAL = 382,
     TOK_RROTATE = 383,
     TOK_LROTATE = 384,
     TOK_RSHIFT = 385,
     TOK_LSHIFT = 386,
     TOK_SETIN = 387,
     TOK_UNION = 388,
     TOK_DIVIDE = 389,
     TOK_TIMES = 390,
     TOK_MINUS = 391,
     TOK_PLUS = 392,
     TOK_MOD = 393,
     TOK_CONCATENATION = 394,
     TOK_SMALLINIT = 395,
     TOK_NEXT = 396,
     TOK_BIT = 397,
     TOK_DOT = 398,
     TOK_LB = 399
   };
#endif
/* Tokens.  */
#define TOK_ITYPE 258
#define TOK_CONSTRAINT 259
#define TOK_MAXU 260
#define TOK_MINU 261
#define TOK_ABU 262
#define TOK_EBU 263
#define TOK_AU 264
#define TOK_EU 265
#define TOK_CONTEXT 266
#define TOK_PROCESS 267
#define TOK_MODULE 268
#define TOK_NAME 269
#define TOK_COMPUTE 270
#define TOK_LTLSPEC 271
#define TOK_CTLSPEC 272
#define TOK_SPEC 273
#define TOK_INVAR 274
#define TOK_TRANS 275
#define TOK_INIT 276
#define TOK_ARRAY_DEFINE 277
#define TOK_DEFINE 278
#define TOK_FUN 279
#define TOK_IVAR 280
#define TOK_FROZENVAR 281
#define TOK_VAR 282
#define TOK_PSLSPEC 283
#define TOK_CONSTANTS 284
#define TOK_JUSTICE 285
#define TOK_COMPASSION 286
#define TOK_FAIRNESS 287
#define TOK_INVARSPEC 288
#define TOK_ASSIGN 289
#define TOK_ISA 290
#define TOK_SEMI 291
#define TOK_CONS 292
#define TOK_OF 293
#define TOK_RCB 294
#define TOK_LCB 295
#define TOK_RB 296
#define TOK_RP 297
#define TOK_LP 298
#define TOK_TWODOTS 299
#define TOK_EQDEF 300
#define TOK_SELF 301
#define TOK_COLON 302
#define TOK_ESAC 303
#define TOK_CASE 304
#define TOK_COMPID 305
#define TOK_COMPWFF 306
#define TOK_CTLWFF 307
#define TOK_LTLPSL 308
#define TOK_LTLWFF 309
#define TOK_NEXTWFF 310
#define TOK_SIMPWFF 311
#define TOK_INCONTEXT 312
#define TOK_WORD 313
#define TOK_BOOLEAN 314
#define TOK_ARRAY 315
#define TOK_WORD1 316
#define TOK_BOOL 317
#define TOK_WAWRITE 318
#define TOK_WAREAD 319
#define TOK_CONST_ARRAY 320
#define TOK_COUNT 321
#define TOK_WTOINT 322
#define TOK_WSIZEOF 323
#define TOK_WRESIZE 324
#define TOK_SWCONST 325
#define TOK_UWCONST 326
#define TOK_EXTEND 327
#define TOK_UNSIGNED 328
#define TOK_SIGNED 329
#define TOK_TYPEOF 330
#define TOK_TRUEEXP 331
#define TOK_FALSEEXP 332
#define TOK_ATOM 333
#define TOK_NUMBER_EXP 334
#define TOK_NUMBER_REAL 335
#define TOK_NUMBER_FRAC 336
#define TOK_NUMBER 337
#define TOK_NUMBER_WORD 338
#define TOK_MAX 339
#define TOK_MIN 340
#define TOK_ABS 341
#define TOK_QUESTIONMARK 342
#define TOK_NOT 343
#define TOK_AND 344
#define TOK_XNOR 345
#define TOK_XOR 346
#define TOK_OR 347
#define TOK_IFF 348
#define TOK_IMPLIES 349
#define TOK_COMMA 350
#define TOK_AA 351
#define TOK_EE 352
#define TOK_AG 353
#define TOK_EG 354
#define TOK_AF 355
#define TOK_EF 356
#define TOK_AX 357
#define TOK_EX 358
#define TOK_RELEASES 359
#define TOK_TRIGGERED 360
#define TOK_UNTIL 361
#define TOK_SINCE 362
#define TOK_MMAX 363
#define TOK_MMIN 364
#define TOK_BUNTIL 365
#define TOK_ABG 366
#define TOK_ABF 367
#define TOK_EBG 368
#define TOK_EBF 369
#define TOK_OP_FUTURE 370
#define TOK_OP_GLOBAL 371
#define TOK_OP_NEXT 372
#define TOK_OP_ONCE 373
#define TOK_OP_HISTORICAL 374
#define TOK_OP_NOTPRECNOT 375
#define TOK_OP_PREC 376
#define TOK_GE 377
#define TOK_LE 378
#define TOK_GT 379
#define TOK_LT 380
#define TOK_NOTEQUAL 381
#define TOK_EQUAL 382
#define TOK_RROTATE 383
#define TOK_LROTATE 384
#define TOK_RSHIFT 385
#define TOK_LSHIFT 386
#define TOK_SETIN 387
#define TOK_UNION 388
#define TOK_DIVIDE 389
#define TOK_TIMES 390
#define TOK_MINUS 391
#define TOK_PLUS 392
#define TOK_MOD 393
#define TOK_CONCATENATION 394
#define TOK_SMALLINIT 395
#define TOK_NEXT 396
#define TOK_BIT 397
#define TOK_DOT 398
#define TOK_LB 399




/* Copy the first part of user declarations.  */
#line 43 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"


#if HAVE_CONFIG_H
# include "nusmv-config.h"
#endif

#include <setjmp.h>

#if NUSMV_HAVE_MALLOC_H
# if NUSMV_HAVE_SYS_TYPES_H
#  include <sys/types.h>
# endif
# include <malloc.h>
#elif defined(NUSMV_HAVE_SYS_MALLOC_H) && NUSMV_HAVE_SYS_MALLOC_H
# if NUSMV_HAVE_SYS_TYPES_H
#  include <sys/types.h>
# endif
# include <sys/malloc.h>
#elif NUSMV_HAVE_STDLIB_H
# include <stdlib.h>
#endif

#include <limits.h>

#include "nusmv/core/parser/parserInt.h"
#include "nusmv/core/parser/psl/pslInt.h"
#include "nusmv/core/utils/utils.h"
#include "nusmv/core/utils/ustring.h"
#include "nusmv/core/node/node.h"
#include "nusmv/core/opt/opt.h"
#include "nusmv/core/prop/propPkg.h"
#include "nusmv/core/utils/ErrorMgr.h"

#include "nusmv/core/parser/symbols.h"
#include "nusmv/core/cinit/NuSMVEnv.h"
#define YYMAXDEPTH INT_MAX

#define GET_OPTS                                                \
  OPTS_HANDLER(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_OPTS_HANDLER))

  /* OPTIMIZATION[REAMa] Test performances. If poor, use ad-hoc variable */
#define NODEMGR                                                         \
  NODE_MGR(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_NODE_MGR))

#define SYNTAX_ERROR_HANDLING(dest, src) \
  {                                      \
    if (OptsHandler_get_bool_option_value(GET_OPTS, \
                                          OPT_PARSER_IS_LAX)) {         \
      dest = src;                                                       \
    }                                                                   \
    else {                                                              \
      YYABORT;                                                          \
    }                                                                   \
 }


node_ptr parsed_tree; /* the returned value of parsing */

/* TODO[AMa] Dirty hack. This var must be updated before all calls of the
   parser */
NuSMVEnv_ptr __nusmv_parser_env__;

enum PARSE_MODE parse_mode_flag; /* the flag what should be parsed */

extern int nusmv_yylineno;
int nusmv_yywrap(void);
void nusmv_yyerror(char *s);
void nusmv_yyerror_lined(const char *s, int line);
static node_ptr node2maincontext(node_ptr node);

/* this enum is used to distinguish
   different kinds of expressions: SIMPLE, NEXT, CTL and LTL.
   Since syntactically only one global kind of expressions exists,
   we have to invoke a special function which checks that an expression
   complies to the additional syntactic constrains.
   So, if a ctl-expression is expected then occurrences of NEXT
   operator will cause the termination of parsing.

   NB: An alternative to invoking a checking function would be to write quite
   intricate syntactic rules to distinguish all the cases.

   NB: This checking function could also be a part of the type checker,
   but it is more straightforward to write a separate function.
*/
  enum EXP_KIND {EXP_SIMPLE, EXP_NEXT, EXP_LTL, EXP_CTL};

  static boolean isCorrectExp(node_ptr exp, enum EXP_KIND expectedKind);

  static node_ptr build_case_colon_node(node_ptr l,
                                        node_ptr r,
                                        int linum);

  static int nusmv_parse_psl(void);


/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif

#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 138 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
{
  node_ptr node;
  int lineno;
}
/* Line 193 of yacc.c.  */
#line 492 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.c"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif



/* Copy the second part of user declarations.  */


/* Line 216 of yacc.c.  */
#line 505 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int i)
#else
static int
YYID (i)
    int i;
#endif
{
  return i;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef _STDLIB_H
#      define _STDLIB_H 1
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined _STDLIB_H \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef _STDLIB_H
#    define _STDLIB_H 1
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss;
  YYSTYPE yyvs;
  };

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yyi;				\
	  for (yyi = 0; yyi < (Count); yyi++)	\
	    (To)[yyi] = (From)[yyi];		\
	}					\
      while (YYID (0))
#  endif
# endif

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack)					\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack, Stack, yysize);				\
	Stack = &yyptr->Stack;						\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  5
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   2526

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  145
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  117
/* YYNRULES -- Number of rules.  */
#define YYNRULES  336
/* YYNRULES -- Number of states.  */
#define YYNSTATES  723

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   399

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,   101,   102,   103,   104,
     105,   106,   107,   108,   109,   110,   111,   112,   113,   114,
     115,   116,   117,   118,   119,   120,   121,   122,   123,   124,
     125,   126,   127,   128,   129,   130,   131,   132,   133,   134,
     135,   136,   137,   138,   139,   140,   141,   142,   143,   144
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     5,     8,    10,    13,    16,    18,    20,
      22,    24,    28,    32,    34,    36,    43,    50,    55,    60,
      62,    64,    66,    68,    70,    72,    74,    79,    81,    84,
      86,    88,    92,    96,   101,   108,   112,   117,   124,   131,
     134,   139,   144,   149,   154,   159,   166,   173,   177,   184,
     193,   203,   208,   210,   214,   216,   219,   224,   226,   230,
     232,   236,   238,   242,   246,   250,   252,   256,   260,   264,
     266,   270,   274,   276,   280,   284,   286,   290,   294,   296,
     300,   304,   306,   308,   312,   314,   318,   320,   324,   326,
     330,   332,   336,   340,   344,   348,   352,   356,   358,   360,
     363,   366,   369,   372,   375,   378,   385,   392,   400,   408,
     412,   416,   420,   424,   427,   429,   433,   435,   439,   443,
     447,   449,   453,   455,   459,   461,   463,   465,   468,   471,
     474,   477,   485,   488,   496,   499,   507,   510,   518,   521,
     523,   527,   531,   535,   539,   541,   545,   547,   551,   555,
     559,   561,   567,   569,   573,   575,   579,   581,   583,   585,
     587,   589,   596,   603,   605,   610,   616,   622,   624,   628,
     636,   641,   645,   647,   649,   652,   654,   658,   660,   662,
     664,   666,   668,   672,   674,   678,   683,   688,   690,   694,
     696,   699,   703,   705,   709,   714,   716,   720,   721,   724,
     727,   729,   731,   733,   735,   737,   739,   741,   743,   745,
     747,   749,   751,   753,   755,   757,   759,   761,   763,   765,
     767,   769,   772,   774,   777,   779,   782,   784,   787,   789,
     792,   795,   797,   800,   803,   805,   808,   811,   813,   816,
     819,   824,   829,   834,   839,   843,   845,   849,   852,   853,
     856,   859,   864,   869,   872,   873,   879,   882,   886,   890,
     892,   896,   900,   902,   905,   906,   909,   912,   917,   925,
     933,   937,   941,   945,   949,   953,   961,   964,   969,   972,
     978,   981,   986,   989,   992,   998,  1004,  1007,  1012,  1015,
    1021,  1024,  1029,  1032,  1038,  1040,  1044,  1045,  1047,  1051,
    1054,  1055,  1057,  1059,  1063,  1067,  1072,  1078,  1080,  1082,
    1086,  1090,  1095,  1097,  1100,  1102,  1106,  1110,  1114,  1118,
    1122,  1125,  1128,  1131,  1134,  1137,  1141,  1143,  1147,  1152,
    1155,  1160,  1161,  1164,  1165,  1168,  1169
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     258,     0,    -1,    82,    -1,   137,    82,    -1,    82,    -1,
     137,    82,    -1,   136,    82,    -1,    83,    -1,    81,    -1,
      80,    -1,    79,    -1,   147,    44,   147,    -1,   167,    44,
     167,    -1,    77,    -1,    76,    -1,    71,    43,   190,    95,
     168,    42,    -1,    70,    43,   190,    95,   168,    42,    -1,
      68,    43,   191,    42,    -1,    67,    43,   191,    42,    -1,
     146,    -1,   148,    -1,   149,    -1,   151,    -1,   150,    -1,
     157,    -1,   156,    -1,   155,    43,   201,    42,    -1,   154,
      -1,   136,   157,    -1,    78,    -1,    46,    -1,   157,   143,
      78,    -1,   157,   143,    82,    -1,   157,   144,   191,    41,
      -1,   157,   144,   190,    47,   190,    41,    -1,    43,   189,
      42,    -1,    86,    43,   189,    42,    -1,    85,    43,   189,
      95,   189,    42,    -1,    84,    43,   189,    95,   189,    42,
      -1,    88,   157,    -1,    62,    43,   189,    42,    -1,    61,
      43,   189,    42,    -1,   141,    43,   189,    42,    -1,    74,
      43,   189,    42,    -1,    73,    43,   189,    42,    -1,    72,
      43,   189,    95,   189,    42,    -1,    69,    43,   189,    95,
     189,    42,    -1,    49,   159,    48,    -1,    64,    43,   189,
      95,   189,    42,    -1,    63,    43,   189,    95,   189,    95,
     189,    42,    -1,    65,    43,    75,    43,   253,    42,    95,
     189,    42,    -1,    66,    43,   158,    42,    -1,   189,    -1,
     189,    95,   158,    -1,   160,    -1,   160,   159,    -1,   189,
      47,   189,    36,    -1,   157,    -1,   161,   139,   157,    -1,
     155,    -1,   162,   139,   155,    -1,   161,    -1,   163,   135,
     161,    -1,   163,   134,   161,    -1,   163,   138,   161,    -1,
     162,    -1,   164,   135,   162,    -1,   164,   134,   162,    -1,
     164,   138,   162,    -1,   163,    -1,   165,   137,   163,    -1,
     165,   136,   163,    -1,   164,    -1,   166,   137,   164,    -1,
     166,   136,   164,    -1,   165,    -1,   167,   131,   165,    -1,
     167,   130,   165,    -1,   166,    -1,   168,   131,   166,    -1,
     168,   130,   166,    -1,   168,    -1,   152,    -1,    40,   170,
      39,    -1,   189,    -1,   170,    95,   189,    -1,   169,    -1,
     171,   133,   169,    -1,   171,    -1,   172,   132,   171,    -1,
     172,    -1,   173,   127,   172,    -1,   173,   126,   172,    -1,
     173,   125,   172,    -1,   173,   124,   172,    -1,   173,   123,
     172,    -1,   173,   122,   172,    -1,   173,    -1,   175,    -1,
     103,   174,    -1,   102,   174,    -1,   101,   174,    -1,   100,
     174,    -1,    99,   174,    -1,    98,   174,    -1,    96,   144,
     180,   106,   180,    41,    -1,    97,   144,   180,   106,   180,
      41,    -1,    96,   144,   180,   110,   152,   180,    41,    -1,
      97,   144,   180,   110,   152,   180,    41,    -1,   114,   152,
     174,    -1,   112,   152,   174,    -1,   113,   152,   174,    -1,
     111,   152,   174,    -1,    88,   175,    -1,   174,    -1,   176,
      89,   174,    -1,   176,    -1,   177,    92,   176,    -1,   177,
      91,   176,    -1,   177,    90,   176,    -1,   177,    -1,   178,
      93,   177,    -1,   178,    -1,   178,    94,   179,    -1,   179,
      -1,   174,    -1,   182,    -1,   117,   181,    -1,   121,   181,
      -1,   120,   181,    -1,   116,   181,    -1,   116,   144,    82,
      95,    82,    41,   181,    -1,   119,   181,    -1,   119,   144,
      82,    95,    82,    41,   181,    -1,   115,   181,    -1,   115,
     144,    82,    95,    82,    41,   181,    -1,   118,   181,    -1,
     118,   144,    82,    95,    82,    41,   181,    -1,    88,   182,
      -1,   181,    -1,   183,   106,   181,    -1,   183,   107,   181,
      -1,   183,   104,   181,    -1,   183,   105,   181,    -1,   183,
      -1,   184,    89,   183,    -1,   184,    -1,   185,    92,   184,
      -1,   185,    91,   184,    -1,   185,    90,   184,    -1,   185,
      -1,   185,    87,   189,    47,   186,    -1,   186,    -1,   187,
      93,   186,    -1,   187,    -1,   187,    94,   188,    -1,   188,
      -1,   189,    -1,   189,    -1,   189,    -1,   189,    -1,   109,
     144,   192,    95,   192,    41,    -1,   108,   144,   192,    95,
     192,    41,    -1,    59,    -1,    58,   144,   190,    41,    -1,
      73,    58,   144,   190,    41,    -1,    74,    58,   144,   190,
      41,    -1,   153,    -1,    40,   197,    39,    -1,    60,    58,
     144,   190,    41,    38,   195,    -1,    60,   153,    38,   195,
      -1,    60,    38,   195,    -1,   195,    -1,   200,    -1,    12,
     200,    -1,   198,    -1,   197,    95,   198,    -1,   199,    -1,
     147,    -1,    77,    -1,    76,    -1,    78,    -1,   199,   143,
      78,    -1,    78,    -1,    78,    43,    42,    -1,    78,    43,
     201,    42,    -1,    60,   153,    38,   200,    -1,   191,    -1,
     201,    95,   191,    -1,   203,    -1,   202,   203,    -1,    13,
     204,   206,    -1,    78,    -1,    78,    43,    42,    -1,    78,
      43,   205,    42,    -1,    78,    -1,   205,    95,    78,    -1,
      -1,   206,   207,    -1,   206,     1,    -1,   250,    -1,   208,
      -1,   209,    -1,   210,    -1,   211,    -1,   230,    -1,   233,
      -1,   234,    -1,   235,    -1,   222,    -1,   225,    -1,   236,
      -1,   237,    -1,   238,    -1,   240,    -1,   242,    -1,   244,
      -1,   247,    -1,   246,    -1,   248,    -1,    27,    -1,    27,
     212,    -1,    26,    -1,    26,   213,    -1,    25,    -1,    25,
     214,    -1,    24,    -1,    24,   215,    -1,   216,    -1,   212,
     216,    -1,   212,     1,    -1,   217,    -1,   213,   217,    -1,
     213,     1,    -1,   218,    -1,   214,   218,    -1,   214,     1,
      -1,   219,    -1,   215,   219,    -1,   215,     1,    -1,   252,
      47,   196,    36,    -1,   252,    47,   195,    36,    -1,   252,
      47,   195,    36,    -1,   252,    47,   220,    36,    -1,   221,
      94,   195,    -1,   195,    -1,   221,   135,   195,    -1,    23,
     223,    -1,    -1,   223,   224,    -1,   223,     1,    -1,   252,
      45,   191,    36,    -1,   252,    45,   227,    36,    -1,    22,
     226,    -1,    -1,   226,   252,    45,   227,    36,    -1,   226,
       1,    -1,   144,   229,    41,    -1,   144,   228,    41,    -1,
     227,    -1,   227,    95,   228,    -1,   191,    95,   229,    -1,
     191,    -1,    34,   231,    -1,    -1,   231,   232,    -1,   231,
       1,    -1,   253,    45,   190,    36,    -1,   140,    43,   253,
      42,    45,   190,    36,    -1,   141,    43,   253,    42,    45,
     191,    36,    -1,    21,   190,   251,    -1,    19,   190,   251,
      -1,    20,   191,   251,    -1,    32,   190,   251,    -1,    30,
     190,   251,    -1,    31,    43,   190,    95,   190,    42,   251,
      -1,   191,   251,    -1,   191,    57,   256,   251,    -1,    33,
     239,    -1,    33,    14,   253,    45,   239,    -1,   192,   251,
      -1,   192,    57,   256,   251,    -1,    18,   241,    -1,    17,
     241,    -1,    18,    14,   253,    45,   241,    -1,    17,    14,
     253,    45,   241,    -1,   193,   251,    -1,   193,    57,   256,
     251,    -1,    16,   243,    -1,    16,    14,   253,    45,   243,
      -1,   194,   251,    -1,   194,    57,   256,   251,    -1,    15,
     245,    -1,    15,    14,   253,    45,   245,    -1,    28,    -1,
      29,   249,    36,    -1,    -1,   199,    -1,   249,    95,   199,
      -1,    35,    78,    -1,    -1,    36,    -1,    78,    -1,   252,
     143,    78,    -1,   252,   143,    82,    -1,   252,   144,    82,
      41,    -1,   252,   144,   136,    82,    41,    -1,    78,    -1,
      46,    -1,   253,   143,    78,    -1,   253,   143,    82,    -1,
     253,   144,   190,    41,    -1,   255,    -1,     1,    36,    -1,
       1,    -1,    21,   190,    36,    -1,    32,   190,    36,    -1,
      20,   191,    36,    -1,     4,   190,    36,    -1,     3,   195,
      36,    -1,    56,   257,    -1,    55,   239,    -1,    52,   241,
      -1,    54,   243,    -1,    51,   245,    -1,    50,   253,    36,
      -1,    78,    -1,   256,   143,    78,    -1,   256,   144,   190,
      41,    -1,   190,   251,    -1,   190,    57,   256,   251,    -1,
      -1,   259,   202,    -1,    -1,   260,   254,    -1,    -1,   261,
     193,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   252,   252,   253,   256,   257,   258,   262,   264,   266,
     268,   271,   275,   279,   280,   281,   283,   285,   287,   289,
     290,   291,   296,   301,   310,   311,   318,   337,   338,   339,
     340,   341,   350,   359,   365,   370,   371,   376,   379,   382,
     383,   384,   385,   386,   387,   388,   389,   390,   392,   395,
     398,   400,   405,   406,   410,   421,   425,   431,   432,   437,
     438,   443,   444,   445,   446,   450,   451,   452,   453,   458,
     459,   460,   465,   466,   467,   470,   471,   472,   475,   476,
     477,   483,   484,   485,   488,   489,   493,   494,   497,   498,
     502,   503,   504,   505,   506,   507,   508,   511,   512,   516,
     517,   518,   519,   520,   521,   522,   524,   526,   528,   530,
     531,   532,   533,   536,   542,   543,   546,   547,   548,   549,
     552,   553,   557,   558,   561,   565,   566,   571,   572,   573,
     574,   575,   577,   578,   580,   581,   583,   584,   587,   594,
     595,   597,   599,   606,   616,   617,   621,   622,   623,   624,
     628,   629,   633,   634,   638,   639,   643,   650,   653,   656,
     659,   663,   665,   674,   675,   677,   679,   681,   682,   684,
     686,   688,   694,   695,   696,   700,   701,   704,   705,   706,
     707,   710,   711,   714,   715,   716,   718,   730,   731,   743,
     744,   747,   750,   751,   752,   755,   756,   761,   762,   763,
     766,   767,   768,   769,   770,   771,   772,   773,   774,   775,
     776,   777,   778,   779,   780,   781,   782,   783,   784,   785,
     794,   795,   798,   799,   802,   803,   805,   809,   815,   816,
     817,   819,   820,   821,   823,   824,   825,   827,   828,   829,
     832,   834,   836,   838,   841,   845,   846,   850,   853,   854,
     855,   858,   860,   873,   877,   878,   879,   883,   884,   888,
     889,   893,   894,   898,   900,   901,   902,   904,   906,   911,
     919,   921,   923,   927,   930,   933,   939,   940,   942,   943,
     946,   947,   949,   950,   951,   952,   955,   956,   959,   960,
     963,   964,   966,   967,   971,   981,   986,   987,   988,   995,
     999,   999,  1007,  1008,  1009,  1010,  1011,  1020,  1021,  1022,
    1023,  1024,  1031,  1032,  1033,  1036,  1038,  1040,  1042,  1044,
    1048,  1049,  1050,  1051,  1052,  1053,  1057,  1058,  1059,  1062,
    1063,  1069,  1069,  1079,  1079,  1086,  1086
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "TOK_ITYPE", "TOK_CONSTRAINT",
  "TOK_MAXU", "TOK_MINU", "TOK_ABU", "TOK_EBU", "TOK_AU", "TOK_EU",
  "TOK_CONTEXT", "TOK_PROCESS", "TOK_MODULE", "TOK_NAME", "TOK_COMPUTE",
  "TOK_LTLSPEC", "TOK_CTLSPEC", "TOK_SPEC", "TOK_INVAR", "TOK_TRANS",
  "TOK_INIT", "TOK_ARRAY_DEFINE", "TOK_DEFINE", "TOK_FUN", "TOK_IVAR",
  "TOK_FROZENVAR", "TOK_VAR", "TOK_PSLSPEC", "TOK_CONSTANTS",
  "TOK_JUSTICE", "TOK_COMPASSION", "TOK_FAIRNESS", "TOK_INVARSPEC",
  "TOK_ASSIGN", "TOK_ISA", "TOK_SEMI", "TOK_CONS", "TOK_OF", "TOK_RCB",
  "TOK_LCB", "TOK_RB", "TOK_RP", "TOK_LP", "TOK_TWODOTS", "TOK_EQDEF",
  "TOK_SELF", "TOK_COLON", "TOK_ESAC", "TOK_CASE", "TOK_COMPID",
  "TOK_COMPWFF", "TOK_CTLWFF", "TOK_LTLPSL", "TOK_LTLWFF", "TOK_NEXTWFF",
  "TOK_SIMPWFF", "TOK_INCONTEXT", "TOK_WORD", "TOK_BOOLEAN", "TOK_ARRAY",
  "TOK_WORD1", "TOK_BOOL", "TOK_WAWRITE", "TOK_WAREAD", "TOK_CONST_ARRAY",
  "TOK_COUNT", "TOK_WTOINT", "TOK_WSIZEOF", "TOK_WRESIZE", "TOK_SWCONST",
  "TOK_UWCONST", "TOK_EXTEND", "TOK_UNSIGNED", "TOK_SIGNED", "TOK_TYPEOF",
  "TOK_TRUEEXP", "TOK_FALSEEXP", "TOK_ATOM", "TOK_NUMBER_EXP",
  "TOK_NUMBER_REAL", "TOK_NUMBER_FRAC", "TOK_NUMBER", "TOK_NUMBER_WORD",
  "TOK_MAX", "TOK_MIN", "TOK_ABS", "TOK_QUESTIONMARK", "TOK_NOT",
  "TOK_AND", "TOK_XNOR", "TOK_XOR", "TOK_OR", "TOK_IFF", "TOK_IMPLIES",
  "TOK_COMMA", "TOK_AA", "TOK_EE", "TOK_AG", "TOK_EG", "TOK_AF", "TOK_EF",
  "TOK_AX", "TOK_EX", "TOK_RELEASES", "TOK_TRIGGERED", "TOK_UNTIL",
  "TOK_SINCE", "TOK_MMAX", "TOK_MMIN", "TOK_BUNTIL", "TOK_ABG", "TOK_ABF",
  "TOK_EBG", "TOK_EBF", "TOK_OP_FUTURE", "TOK_OP_GLOBAL", "TOK_OP_NEXT",
  "TOK_OP_ONCE", "TOK_OP_HISTORICAL", "TOK_OP_NOTPRECNOT", "TOK_OP_PREC",
  "TOK_GE", "TOK_LE", "TOK_GT", "TOK_LT", "TOK_NOTEQUAL", "TOK_EQUAL",
  "TOK_RROTATE", "TOK_LROTATE", "TOK_RSHIFT", "TOK_LSHIFT", "TOK_SETIN",
  "TOK_UNION", "TOK_DIVIDE", "TOK_TIMES", "TOK_MINUS", "TOK_PLUS",
  "TOK_MOD", "TOK_CONCATENATION", "TOK_SMALLINIT", "TOK_NEXT", "TOK_BIT",
  "TOK_DOT", "TOK_LB", "$accept", "number", "integer", "number_word",
  "number_frac", "number_real", "number_exp", "subrange", "subrangetype",
  "constant", "primary_expr", "nfunc_expr", "primary_expr_type",
  "count_param_list", "case_element_list_expr", "case_element_expr",
  "concatination_expr_type", "concatination_expr",
  "multiplicative_expr_type", "multiplicative_expr", "additive_expr_type",
  "additive_expr", "shift_expr_type", "shift_expr", "set_expr",
  "set_list_expr", "union_expr", "in_expr", "relational_expr", "ctl_expr",
  "pure_ctl_expr", "ctl_and_expr", "ctl_or_expr", "ctl_iff_expr",
  "ctl_implies_expr", "ctl_basic_expr", "ltl_unary_expr",
  "pure_ltl_unary_expr", "ltl_binary_expr", "and_expr", "or_expr",
  "ite_expr", "iff_expr", "implies_expr", "basic_expr",
  "simple_expression", "next_expression", "ctl_expression",
  "ltl_expression", "compute_expression", "itype", "type",
  "type_value_list", "type_value", "complex_atom", "module_type",
  "next_list_expression", "module_list", "module", "module_sign",
  "atom_list", "declarations", "declaration", "var", "frozen_var",
  "input_var", "fun_def", "var_decl_list", "fvar_decl_list",
  "ivar_decl_list", "fun_decl_list", "var_decl", "fvar_decl", "ivar_decl",
  "fun_decl", "nfun_type", "nfun_ftype", "define_decls", "define_list",
  "define", "array_define", "array_define_list", "array_expression",
  "array_expression_list", "array_contents", "assign", "assign_list",
  "one_assign", "init", "invar", "trans", "fairness", "justice",
  "compassion", "_invarspec", "invarspec", "_ctlspec", "ctlspec",
  "_ltlspec", "ltlspec", "_compute", "compute", "pslspec", "constants",
  "constants_expression", "isa", "optsemi", "decl_var_id", "var_id",
  "command", "command_case", "context", "_simpwff", "begin", "@1", "@2",
  "@3", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   341,   342,   343,   344,
     345,   346,   347,   348,   349,   350,   351,   352,   353,   354,
     355,   356,   357,   358,   359,   360,   361,   362,   363,   364,
     365,   366,   367,   368,   369,   370,   371,   372,   373,   374,
     375,   376,   377,   378,   379,   380,   381,   382,   383,   384,
     385,   386,   387,   388,   389,   390,   391,   392,   393,   394,
     395,   396,   397,   398,   399
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint16 yyr1[] =
{
       0,   145,   146,   146,   147,   147,   147,   148,   149,   150,
     151,   152,   153,   154,   154,   154,   154,   154,   154,   154,
     154,   154,   154,   154,   155,   155,   156,   157,   157,   157,
     157,   157,   157,   157,   157,   157,   157,   157,   157,   157,
     157,   157,   157,   157,   157,   157,   157,   157,   157,   157,
     157,   157,   158,   158,   159,   159,   160,   161,   161,   162,
     162,   163,   163,   163,   163,   164,   164,   164,   164,   165,
     165,   165,   166,   166,   166,   167,   167,   167,   168,   168,
     168,   169,   169,   169,   170,   170,   171,   171,   172,   172,
     173,   173,   173,   173,   173,   173,   173,   174,   174,   175,
     175,   175,   175,   175,   175,   175,   175,   175,   175,   175,
     175,   175,   175,   175,   176,   176,   177,   177,   177,   177,
     178,   178,   179,   179,   180,   181,   181,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   183,
     183,   183,   183,   183,   184,   184,   185,   185,   185,   185,
     186,   186,   187,   187,   188,   188,   189,   190,   191,   192,
     193,   194,   194,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   196,   196,   196,   197,   197,   198,   198,   198,
     198,   199,   199,   200,   200,   200,   200,   201,   201,   202,
     202,   203,   204,   204,   204,   205,   205,   206,   206,   206,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     208,   208,   209,   209,   210,   210,   211,   211,   212,   212,
     212,   213,   213,   213,   214,   214,   214,   215,   215,   215,
     216,   217,   218,   219,   220,   221,   221,   222,   223,   223,
     223,   224,   224,   225,   226,   226,   226,   227,   227,   228,
     228,   229,   229,   230,   231,   231,   231,   232,   232,   232,
     233,   234,   235,   236,   237,   238,   239,   239,   240,   240,
     241,   241,   242,   242,   242,   242,   243,   243,   244,   244,
     245,   245,   246,   246,   247,   248,   249,   249,   249,   250,
     251,   251,   252,   252,   252,   252,   252,   253,   253,   253,
     253,   253,   254,   254,   254,   255,   255,   255,   255,   255,
     255,   255,   255,   255,   255,   255,   256,   256,   256,   257,
     257,   259,   258,   260,   258,   261,   258
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     2,     2,     1,     1,     1,
       1,     3,     3,     1,     1,     6,     6,     4,     4,     1,
       1,     1,     1,     1,     1,     1,     4,     1,     2,     1,
       1,     3,     3,     4,     6,     3,     4,     6,     6,     2,
       4,     4,     4,     4,     4,     6,     6,     3,     6,     8,
       9,     4,     1,     3,     1,     2,     4,     1,     3,     1,
       3,     1,     3,     3,     3,     1,     3,     3,     3,     1,
       3,     3,     1,     3,     3,     1,     3,     3,     1,     3,
       3,     1,     1,     3,     1,     3,     1,     3,     1,     3,
       1,     3,     3,     3,     3,     3,     3,     1,     1,     2,
       2,     2,     2,     2,     2,     6,     6,     7,     7,     3,
       3,     3,     3,     2,     1,     3,     1,     3,     3,     3,
       1,     3,     1,     3,     1,     1,     1,     2,     2,     2,
       2,     7,     2,     7,     2,     7,     2,     7,     2,     1,
       3,     3,     3,     3,     1,     3,     1,     3,     3,     3,
       1,     5,     1,     3,     1,     3,     1,     1,     1,     1,
       1,     6,     6,     1,     4,     5,     5,     1,     3,     7,
       4,     3,     1,     1,     2,     1,     3,     1,     1,     1,
       1,     1,     3,     1,     3,     4,     4,     1,     3,     1,
       2,     3,     1,     3,     4,     1,     3,     0,     2,     2,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     2,     1,     2,     1,     2,     1,     2,     1,     2,
       2,     1,     2,     2,     1,     2,     2,     1,     2,     2,
       4,     4,     4,     4,     3,     1,     3,     2,     0,     2,
       2,     4,     4,     2,     0,     5,     2,     3,     3,     1,
       3,     3,     1,     2,     0,     2,     2,     4,     7,     7,
       3,     3,     3,     3,     3,     7,     2,     4,     2,     5,
       2,     4,     2,     2,     5,     5,     2,     4,     2,     5,
       2,     4,     2,     5,     1,     3,     0,     1,     3,     2,
       0,     1,     1,     3,     3,     4,     5,     1,     1,     3,
       3,     4,     1,     2,     1,     3,     3,     3,     3,     3,
       2,     2,     2,     2,     2,     3,     1,     3,     4,     2,
       4,     0,     2,     0,     2,     0,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
     335,     0,     0,     0,     0,     1,     0,   332,   189,   314,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   334,   312,     0,     0,    30,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    14,    13,    29,    10,     9,     8,     2,     7,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    19,     0,    20,    21,    23,
      22,    82,    27,    59,    25,    24,    65,    72,    78,    81,
      86,    88,    90,    97,   125,    98,   139,   126,   144,   146,
     150,   152,   154,   156,   160,   336,   192,   197,   190,   313,
       0,     0,   163,     0,     0,     0,     2,     0,     0,     0,
     167,    57,    61,    69,    75,     0,     0,   157,     0,   158,
       0,     0,     0,   308,   307,     0,     0,     0,   300,   324,
     159,   300,   322,   300,   323,   300,   321,   300,   320,     0,
      84,     0,     0,    54,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    39,   113,   138,     0,     0,     0,   104,   103,
     102,   101,   100,    99,     4,     0,     0,     0,     0,     0,
       0,     0,   134,     0,   130,   127,     0,   136,     0,   132,
     129,   128,     2,    28,     3,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   180,
     179,   181,   178,     0,   175,   177,     0,     0,     0,     0,
       0,     0,     3,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   319,   318,   317,   315,   316,   325,     0,     0,
       0,     0,   301,     0,   290,     0,   280,     0,   286,     0,
     276,     0,   329,    83,     0,    35,    47,    55,     0,     0,
       0,     0,     0,     0,     0,    52,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   114,   116,   120,
     122,   124,     0,     0,     6,     5,   112,   110,   111,   109,
       0,     0,     0,     0,     0,    11,   187,     0,    31,    32,
     157,     0,     0,    60,    67,    66,    68,    74,    73,    80,
      79,    87,    89,    96,    95,    94,    93,    92,    91,   142,
     143,   140,   141,   145,     0,   149,   148,   147,   153,   155,
     193,   195,     0,   199,     0,     0,     0,     0,     0,     0,
       0,   254,   248,   226,   224,   222,   220,   294,   296,     0,
       0,     0,     0,   264,     0,   198,   201,   202,   203,   204,
     209,   210,   205,   206,   207,   208,   211,   212,   213,   214,
     215,   216,   218,   217,   219,   200,   168,     0,     0,     0,
     171,     0,     0,     0,     0,    58,    63,    62,    64,    71,
      70,    12,    77,    76,   309,   310,     0,     0,     0,   326,
     300,   300,   300,   300,   300,    85,     0,    41,    40,     0,
       0,     0,    51,     0,    18,    17,     0,     0,     0,     0,
      44,    43,     0,     0,    36,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    42,
      26,     0,     0,    33,     0,   194,     0,     0,   292,     0,
     288,     0,   283,     0,   282,   300,   300,   300,     0,     0,
     302,     0,   237,     0,     0,   234,     0,     0,   231,     0,
       0,   228,     0,   297,     0,   300,     0,   300,     0,   278,
       0,   299,   176,   182,   164,     0,   170,     0,     0,   311,
       0,     0,     0,     0,   291,   281,   287,   277,   330,    56,
       0,     0,     0,    53,     0,     0,     0,     0,     0,     0,
     115,   119,   118,   117,   121,   123,     0,     0,     0,     0,
       0,     0,     0,     0,   188,     0,   151,   196,     0,     0,
       0,     0,   271,   272,   270,   256,     0,   250,   249,     0,
     239,   238,     0,     0,     0,   236,   235,     0,   233,   232,
       0,   230,   229,     0,   295,     0,   274,     0,   273,     0,
     266,     0,     0,   265,     0,     0,   165,   166,     0,     0,
     327,     0,     0,    48,     0,    46,    16,    15,    45,    38,
      37,   105,     0,   106,     0,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,   245,     0,     0,   303,
     304,     0,     0,     0,     0,     0,     0,    29,   172,     0,
     173,   298,     0,     0,     0,     0,     0,     0,   162,   161,
     328,     0,     0,   107,   108,   135,   131,   137,   133,   293,
     289,   285,   284,     0,     0,     0,     0,   243,     0,     0,
     305,     0,   242,   241,     0,   183,   174,     0,     0,   240,
       0,   279,     0,     0,     0,   169,    49,     0,   262,   259,
       0,     0,   255,   251,   252,   244,   246,   306,     0,     0,
     184,     0,   300,     0,     0,   267,    50,     0,     0,   258,
     257,     0,   186,   185,   275,     0,     0,   261,   260,     0,
       0,   268,   269
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,    75,    76,    77,    78,    79,    80,    81,   120,    82,
      83,    84,    85,   294,   152,   153,   122,    86,   123,    87,
     124,    88,   125,    89,    90,   149,    91,    92,    93,    94,
      95,   308,   309,   310,   311,   312,    96,    97,    98,    99,
     100,   101,   102,   103,   127,   128,   145,   141,   143,   138,
     516,   639,   243,   244,   245,   712,   327,     7,     8,   107,
     362,   238,   385,   386,   387,   388,   389,   500,   497,   494,
     491,   501,   498,   495,   492,   627,   628,   390,   489,   568,
     391,   488,   689,   690,   691,   392,   510,   593,   393,   394,
     395,   396,   397,   398,   146,   399,   142,   400,   144,   401,
     139,   402,   403,   404,   504,   405,   274,   493,   135,    21,
      22,   430,   148,     1,     2,     3,     4
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -511
static const yytype_int16 yypact[] =
{
     400,    41,    63,   356,  1703,  -511,   -27,    63,  -511,    60,
    1869,  1703,  1703,  1703,  1703,     6,   -23,  1703,  1703,  1703,
    1703,  -511,  -511,  1703,  1703,  -511,  1703,    71,   105,   107,
     129,   135,   137,   153,   195,   197,   211,   226,   233,   235,
     243,  -511,  -511,  -511,  -511,  -511,  -511,    79,  -511,   259,
     261,   277,  2043,   -77,    82,  1785,  1785,  1785,  1785,  1785,
    1785,   -29,   -29,   -29,   -29,  1154,  1238,  1703,  1322,  1406,
    1703,  1703,  2205,   133,   313,  -511,   314,  -511,  -511,  -511,
    -511,  -511,  -511,   321,  -511,   150,   240,   109,   230,   167,
    -511,   257,   268,   186,  -511,  -511,  -511,  -511,   244,   316,
     161,  -511,   293,  -511,  -511,  -511,   359,  -511,  -511,  -511,
     159,   265,  -511,  1574,    97,   164,  -511,  2249,  2249,   334,
    -511,   150,   280,   136,   262,   101,   395,  -511,   401,  -511,
     405,   417,   427,  -511,  -511,   -26,   320,   322,    54,  -511,
    -511,    64,  -511,    76,  -511,   166,  -511,   168,  -511,     9,
    -511,   423,   420,  1703,   422,  1703,  1703,  1703,  1703,   398,
    1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,
    1703,  1703,   150,  -511,  -511,  1785,  1785,  2124,  -511,  -511,
    -511,  -511,  -511,  -511,  -511,   392,   393,  1785,  1785,  1785,
    1785,   425,  -511,   426,  -511,  -511,   429,  -511,   430,  -511,
    -511,  -511,   465,   150,   474,  1703,   -29,  1703,    31,  1703,
    2249,  2249,  2249,  2249,  2249,  2249,  2249,  2249,  1997,  1997,
    1997,  1997,  1997,  1997,  1997,  1997,  1703,  1703,  1703,  1703,
    1703,  1703,  1703,  1703,  1703,  1703,  1703,    23,   665,  -511,
    -511,  -511,  -511,    11,  -511,   372,  1703,  1869,   375,   482,
     377,   378,  -511,  2249,  2249,  2249,  2249,  2249,  2249,  2249,
    2249,  2249,  -511,  -511,  -511,  -511,  -511,  -511,   146,  1703,
    1703,  1703,  -511,   445,  -511,   445,  -511,   445,  -511,   445,
    -511,   445,  -511,  -511,  1703,  -511,  -511,  -511,  1703,   483,
     508,   456,   457,   510,   512,   460,   514,   515,   463,   464,
     466,   468,   518,   522,   470,   473,   524,  -511,   481,   263,
     332,  -511,   158,   169,  -511,  -511,  -511,  -511,  -511,  -511,
     478,   485,   486,   488,   534,  -511,  -511,     7,  -511,  -511,
     536,   537,   546,   321,   240,   240,   240,   109,   109,   230,
     230,  -511,   257,   268,   268,   268,   268,   268,   268,  -511,
    -511,  -511,  -511,   244,   541,   316,   316,   316,  -511,  -511,
    -511,  -511,    21,  -511,   125,   748,   856,   964,  1703,  1703,
    1703,  -511,  -511,   511,   511,   511,   511,  -511,   516,  1703,
     547,  1703,  1072,  -511,   517,  -511,  -511,  -511,  -511,  -511,
    -511,  -511,  -511,  -511,  -511,  -511,  -511,  -511,  -511,  -511,
    -511,  -511,  -511,  -511,  -511,  -511,  -511,   159,   519,   551,
    -511,  1703,  1869,  1703,  1703,   150,   280,   280,   280,   147,
     147,   297,   262,   262,  -511,  -511,   552,   501,   504,  -511,
     -13,   -13,   -13,   -13,   -13,  -511,   564,  -511,  -511,  1703,
    1703,     6,  -511,  1703,  -511,  -511,  1703,  2249,  2249,  1703,
    -511,  -511,  1703,  1703,  -511,  1785,  1785,  1785,  1785,  1785,
    1785,  1785,   -29,  1785,   -29,   520,   521,   527,   528,  -511,
    -511,  1703,  1703,  -511,  1703,  -511,   523,     6,  -511,     6,
    -511,     6,  -511,     6,  -511,   568,   568,   568,   471,   513,
    -511,  2338,  -511,    47,  2376,  -511,    50,  2412,  -511,    56,
    2448,  -511,    77,   372,    10,   568,  1703,   568,     6,  -511,
     306,  -511,  -511,  -511,  -511,   570,  -511,   571,   572,  -511,
    1703,  1703,   538,  1703,  -511,  -511,  -511,  -511,  -511,  -511,
     525,   573,    -6,  -511,   580,     5,    46,   581,   583,   584,
    -511,   481,   481,   481,   263,  -511,   586,  1785,   587,  1785,
     588,   589,   590,   591,  -511,   592,  -511,  -511,   -17,   -15,
      -2,    27,  -511,  -511,  -511,  -511,    30,  -511,  -511,    38,
    -511,  -511,  1869,   210,   -38,  -511,  -511,  1869,  -511,  -511,
    1869,  -511,  -511,   667,  -511,   516,  -511,   539,  -511,    42,
    -511,   593,   594,  -511,    44,   576,  -511,  -511,   599,   600,
    -511,   602,  1703,  -511,   540,  -511,  -511,  -511,  -511,  -511,
    -511,  -511,   603,  -511,   604,  1703,  1703,  1703,  1703,  -511,
     -23,  1703,  1703,  1703,   503,  1490,  -511,   615,    -3,  -511,
    -511,   611,   574,   617,   618,    32,  1574,   203,  -511,   619,
    -511,   372,  1703,  1703,     6,     6,  1703,  1869,  -511,  -511,
    -511,   616,  1703,  -511,  -511,  -511,  -511,  -511,  -511,  -511,
    -511,  -511,  -511,  1490,   621,   624,   625,  -511,  1869,  1869,
    -511,   626,  -511,  -511,  2249,   629,  -511,   630,  1621,  -511,
     627,  -511,     0,     3,   637,  -511,  -511,   633,   607,   609,
     664,   668,  -511,  -511,  -511,  -511,  -511,  -511,   670,  1916,
    -511,    80,   568,   666,   669,  -511,  -511,  1703,   503,  -511,
    -511,    32,  -511,  -511,  -511,  1703,  1703,  -511,  -511,   681,
     682,  -511,  -511
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -511,  -511,  -107,  -511,  -511,  -511,  -511,   -24,  -112,  -511,
     532,  -511,     2,   278,   567,  -511,   126,   181,   172,   219,
     183,   241,   495,    12,   505,  -511,   542,   122,  -511,    22,
     -43,   -61,   298,  -511,   264,  -174,   -10,   704,   492,   190,
    -511,  -229,  -511,   529,    -4,     4,    -1,  -238,   754,  -511,
      -5,  -511,  -511,   352,  -371,  -510,    85,  -511,   753,  -511,
    -511,  -511,  -511,  -511,  -511,  -511,  -511,  -511,  -511,  -511,
    -511,   266,   267,   273,   279,  -511,  -511,  -511,  -511,  -511,
    -511,  -511,  -163,    61,    65,  -511,  -511,  -511,  -511,  -511,
    -511,  -511,  -511,  -511,  -378,  -511,  -332,  -511,  -349,  -511,
    -343,  -511,  -511,  -511,  -511,  -511,  -116,  -305,  -415,  -511,
    -511,    24,  -511,  -511,  -511,  -511,  -511
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -334
static const yytype_int16 yytable[] =
{
     104,   249,   313,   242,   509,   126,   358,   503,   129,   173,
     267,   130,   121,   140,   104,   129,   480,   131,   132,   150,
     151,   478,   154,   272,   147,   276,   532,   278,   620,   280,
     621,   282,   427,   428,   482,   484,   604,   187,   188,   189,
     190,     5,   703,   622,   631,   704,   584,   606,   283,   470,
     406,   106,   133,   184,   172,   192,   194,   195,   197,   199,
     200,   201,   558,   475,   559,   360,   560,   175,   561,   496,
     499,   502,   623,   640,   203,   624,     6,   178,   179,   180,
     181,   182,   183,   625,   134,   136,   137,   643,   607,   646,
     272,   668,   674,   589,   572,   594,   109,   577,   632,   325,
     272,   361,   471,   580,   284,   585,   407,   185,   186,   328,
     675,   273,   272,   329,   155,   121,   476,   268,   269,   172,
     203,   275,   713,    -4,   583,   676,   268,   269,   268,   269,
     522,   523,   669,   277,   173,   216,   217,   268,   269,   477,
     167,   268,   269,   268,   269,   259,   268,   269,   156,   154,
     157,   289,   290,   291,   292,   250,   295,   129,   129,   298,
     296,   297,   301,   302,   303,   304,   305,   306,   299,   300,
     268,   269,   158,   573,   574,   471,   216,   217,   159,   172,
     160,   573,   574,   566,   569,   268,   269,   268,   269,   496,
     573,   574,   499,   573,   574,   502,   161,   307,   307,   573,
     574,   324,   272,   129,   272,   330,   326,   168,   332,   316,
     317,   318,   319,   331,   641,   204,   349,   350,   351,   352,
     573,   574,   251,   279,   424,   281,   176,   354,   425,   682,
     683,   260,   261,   136,   137,   239,   240,   241,   162,  -183,
     163,   184,   410,   211,   212,   556,   678,   213,   231,   121,
     409,   232,   233,   234,   164,   415,   121,   121,   121,   121,
     121,   121,   121,   121,   461,   681,   140,   140,   462,   165,
     254,   255,   660,   426,   256,   463,   166,   659,   167,   464,
     435,   254,   598,   599,   436,   256,   168,   546,   629,   548,
     661,   662,   630,   208,   209,   185,   186,   216,   217,   431,
     242,   432,   169,   433,   170,   434,  -263,   590,   220,   221,
     222,   223,   224,   225,   524,   525,   526,   527,   528,  -263,
     171,  -263,  -263,  -263,  -263,  -263,  -263,  -263,  -263,  -263,
    -263,  -263,  -263,  -263,  -263,  -263,  -263,  -263,  -263,  -263,
    -263,  -263,   343,   344,   345,   346,   347,   348,   226,   227,
     228,   229,   133,   456,   457,   458,   205,     9,   206,    10,
      11,   104,   140,   140,   207,   129,   214,   215,   486,   562,
     563,   564,   485,   612,   487,   614,    12,    13,   129,   210,
     416,   417,   418,   505,   134,   507,   235,   236,    14,   586,
     218,   588,   334,   335,   336,   541,   542,   543,   257,   258,
     219,  -333,   237,  -333,  -333,   230,    15,    16,    17,   246,
      18,    19,    20,  -331,   121,   515,   252,   517,   518,   253,
    -333,  -333,   355,   356,   357,   459,   460,   260,   261,   419,
     420,   262,  -333,   337,   338,   530,   531,   263,   547,   295,
     549,   264,   534,   422,   423,   537,   591,   592,   538,   539,
    -333,  -333,  -333,   265,  -333,  -333,  -333,   339,   340,   535,
     536,   664,   666,   266,   270,   285,   271,   129,   286,   288,
     554,  -253,   565,   293,   314,   315,   555,   540,   307,   307,
     307,   307,   307,   307,  -253,   307,  -253,  -253,  -253,  -253,
    -253,  -253,  -253,  -253,  -253,  -253,  -253,  -253,  -253,  -253,
    -253,  -253,  -253,  -253,  -253,  -253,  -253,   320,   321,    -6,
     587,   322,   323,  -247,   567,   408,   140,   140,    -5,   411,
     412,   413,   414,   429,   677,   437,  -247,   601,  -247,  -247,
    -247,  -247,  -247,  -247,  -247,  -247,  -247,  -247,  -247,  -247,
    -247,  -247,  -247,  -247,  -247,  -247,  -247,  -247,  -247,   490,
     438,   439,   440,   441,   442,   443,   444,   445,   446,   447,
     450,   448,   698,   449,   451,   452,   454,   626,   453,   307,
     455,   307,   633,   465,   121,   634,   469,  -158,   638,   121,
     466,   467,   121,   468,   472,   121,   714,   473,   474,   490,
     506,   490,   514,   519,   241,   511,   520,   513,   651,   521,
     529,   557,   550,   551,   272,   655,   656,   657,   658,   552,
     553,   595,   596,   597,   647,   603,   600,   104,   140,   140,
     602,   129,   605,   608,   665,   609,   610,   611,   613,   615,
     616,   617,   618,   619,   642,   652,   644,   645,   121,   129,
     648,   649,   685,   650,   653,   654,   680,   663,   687,   121,
     684,   667,   670,   672,   673,   679,   671,   692,   686,   129,
     693,   694,   688,   695,   696,  -191,   363,   697,   699,   702,
     121,   121,   678,   705,   129,   706,   121,   326,  -191,   635,
     364,   365,   366,   367,   368,   369,   370,   371,   372,   373,
     374,   375,   376,   377,   378,   379,   380,   381,   382,   383,
     384,   121,   707,   129,   708,   709,   688,   110,   711,   710,
      24,   715,   129,    25,   716,   720,    26,   721,   722,   719,
     287,   533,   353,   341,   545,   111,   112,   636,    27,    28,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
     114,   115,   333,    41,    42,   637,    44,    45,    46,   116,
      48,    49,    50,    51,   421,   117,   174,   544,   105,   512,
     108,   342,   479,   701,   579,   359,   582,   576,     0,   718,
     571,     0,   717,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    23,     0,
       0,    24,     0,     0,    25,     0,     0,    26,     0,     0,
       0,     0,     0,   118,   119,     0,     0,     0,    74,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,     0,    41,    42,    43,    44,    45,    46,
      47,    48,    49,    50,    51,     0,    52,     0,     0,     0,
       0,     0,     0,     0,    53,    54,    55,    56,    57,    58,
      59,    60,     0,     0,     0,     0,     0,     0,     0,    61,
      62,    63,    64,    65,    66,    67,    68,    69,    70,    71,
     481,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    72,    73,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    23,     0,     0,    24,
       0,     0,    25,     0,     0,    26,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,     0,    41,    42,    43,    44,    45,    46,    47,    48,
      49,    50,    51,     0,    52,     0,     0,     0,     0,     0,
       0,     0,    53,    54,    55,    56,    57,    58,    59,    60,
       0,     0,     0,     0,     0,     0,     0,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,   483,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    72,    73,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    23,     0,     0,    24,     0,     0,
      25,     0,     0,    26,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,     0,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      51,     0,    52,     0,     0,     0,     0,     0,     0,     0,
      53,    54,    55,    56,    57,    58,    59,    60,     0,     0,
       0,     0,     0,     0,     0,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,   508,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      72,    73,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    23,     0,     0,    24,     0,     0,    25,     0,
       0,    26,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,     0,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,     0,
      52,     0,     0,     0,     0,     0,     0,     0,    53,    54,
      55,    56,    57,    58,    59,    60,     0,     0,     0,     0,
       0,     0,     0,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    23,     0,     0,    24,     0,     0,
      25,     0,     0,    26,     0,     0,     0,     0,    72,    73,
       0,     0,     0,    74,     0,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,     0,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      51,     0,    52,     0,     0,     0,     0,     0,     0,     0,
      53,    54,    55,    56,    57,    58,    59,    60,     0,     0,
       0,     0,     0,     0,     0,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,     0,     0,    23,     0,
       0,    24,     0,     0,    25,     0,     0,    26,     0,     0,
      72,    73,     0,     0,     0,    74,     0,     0,   191,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,     0,    41,    42,    43,    44,    45,    46,
      47,    48,    49,    50,    51,     0,    52,     0,     0,     0,
       0,     0,     0,     0,    53,    54,    55,    56,    57,    58,
      59,    60,     0,     0,     0,     0,     0,     0,     0,    61,
      62,    63,    64,    65,    66,    67,    68,    69,    70,    71,
       0,     0,    23,     0,     0,    24,     0,     0,    25,     0,
       0,    26,     0,     0,    72,    73,     0,     0,     0,    74,
       0,     0,   193,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,     0,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,     0,
      52,     0,     0,     0,     0,     0,     0,     0,    53,    54,
      55,    56,    57,    58,    59,    60,     0,     0,     0,     0,
       0,     0,     0,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,     0,     0,    23,     0,     0,    24,
       0,     0,    25,     0,     0,    26,     0,     0,    72,    73,
       0,     0,     0,    74,     0,     0,   196,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,     0,    41,    42,    43,    44,    45,    46,    47,    48,
      49,    50,    51,     0,    52,     0,     0,     0,     0,     0,
       0,     0,    53,    54,    55,    56,    57,    58,    59,    60,
       0,     0,     0,     0,     0,     0,     0,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,     0,     0,
      23,     0,     0,    24,     0,     0,    25,     0,     0,    26,
       0,     0,    72,    73,     0,     0,     0,    74,     0,     0,
     198,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,     0,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,     0,    52,     0,
       0,     0,     0,     0,     0,     0,    53,    54,    55,    56,
      57,    58,    59,    60,     0,     0,     0,     0,     0,     0,
       0,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,   247,     0,     0,     0,     0,    24,     0,     0,
      25,     0,     0,    26,     0,     0,    72,    73,     0,     0,
       0,    74,   248,     0,   663,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,     0,
      41,    42,    43,    44,    45,    46,   116,    48,    49,    50,
      51,    23,   117,   700,    24,     0,     0,    25,     0,     0,
      26,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,     0,    41,    42,    43,
      44,    45,    46,    47,    48,    49,    50,    51,     0,    52,
     118,   119,     0,     0,     0,    74,     0,    53,    54,    55,
      56,    57,    58,    59,    60,     0,     0,     0,     0,     0,
       0,     0,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    23,     0,     0,    24,     0,     0,    25,
       0,     0,    26,     0,     0,     0,     0,    72,    73,     0,
       0,     0,    74,     0,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,     0,    41,
      42,    43,    44,    45,    46,    47,    48,    49,    50,    51,
       0,    52,     0,     0,     0,     0,     0,     0,     0,    53,
      54,    55,    56,    57,    58,    59,    60,     0,     0,     0,
       0,     0,     0,     0,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,    23,     0,     0,    24,     0,
       0,    25,     0,     0,    26,     0,     0,     0,     0,    72,
      73,     0,     0,     0,    74,     0,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    39,    40,
       0,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,     0,   177,     0,     0,     0,     0,     0,     0,
       0,    53,    54,    55,    56,    57,    58,    59,    60,     0,
       0,     0,     0,     0,     0,     0,    61,    62,    63,    64,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   110,
       0,     0,    24,     0,     0,    25,     0,     0,    26,     0,
       0,    72,    73,     0,     0,     0,    74,   111,   112,   113,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,   114,   115,     0,    41,    42,    43,    44,    45,
      46,   116,    48,    49,    50,    51,   110,   117,     0,    24,
       0,     0,    25,     0,     0,    26,     0,     0,     0,     0,
       0,     0,     0,     0,   111,   112,   636,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,   114,
     115,     0,    41,    42,   637,    44,    45,    46,   116,    48,
      49,    50,    51,     0,   117,   118,   119,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    23,     0,     0,
      24,     0,     0,    25,     0,     0,    26,     0,     0,     0,
       0,     0,   118,   119,     0,     0,     0,    74,    27,    28,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
      39,    40,     0,    41,    42,    43,    44,    45,    46,    47,
      48,    49,    50,    51,     0,   117,    24,     0,     0,    25,
       0,     0,    26,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,     0,    41,
      42,    43,    44,    45,    46,   116,    48,    49,    50,    51,
       0,    52,     0,    72,    73,     0,     0,     0,    74,    53,
      54,    55,    56,    57,    58,    59,    60,     0,     0,     0,
       0,     0,     0,     0,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,     0,     0,    24,     0,     0,
      25,     0,     0,    26,     0,     0,     0,     0,     0,   118,
     119,     0,     0,     0,    74,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,     0,
      41,    42,    43,    44,    45,    46,   116,    48,    49,    50,
      51,     0,   177,     0,     0,     0,     0,     0,     0,     0,
      53,    54,    55,    56,    57,    58,    59,    60,     0,     0,
       0,     0,     0,     0,     0,    61,    62,    63,    64,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    24,     0,
       0,    25,     0,     0,    26,     0,     0,     0,     0,     0,
     118,   119,     0,     0,     0,    74,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    39,    40,
       0,    41,    42,    43,    44,    45,    46,   202,    48,    49,
      50,    51,    24,   117,     0,    25,     0,     0,    26,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,     0,    41,    42,    43,    44,    45,
      46,   116,    48,    49,    50,    51,     0,   117,  -227,   570,
       0,   118,   119,     0,     0,     0,    74,     0,     0,     0,
       0,  -227,     0,  -227,  -227,  -227,  -227,  -227,  -227,  -227,
    -227,  -227,  -227,  -227,  -227,  -227,  -227,  -227,  -227,  -227,
    -227,  -227,  -227,  -227,     0,     0,  -225,   575,     0,     0,
       0,     0,     0,     0,     0,   118,   119,     0,     0,  -225,
      74,  -225,  -225,  -225,  -225,  -225,  -225,  -225,  -225,  -225,
    -225,  -225,  -225,  -225,  -225,  -225,  -225,  -225,  -225,  -225,
    -225,  -225,  -223,   578,     0,     0,   490,     0,     0,     0,
       0,     0,     0,     0,     0,  -223,     0,  -223,  -223,  -223,
    -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,
    -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,  -221,   581,
       0,     0,     0,     0,   490,     0,     0,     0,     0,     0,
       0,  -221,     0,  -221,  -221,  -221,  -221,  -221,  -221,  -221,
    -221,  -221,  -221,  -221,  -221,  -221,  -221,  -221,  -221,  -221,
    -221,  -221,  -221,  -221,     0,     0,     0,     0,     0,     0,
     490,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   490
};

static const yytype_int16 yycheck[] =
{
       4,   113,   176,   110,   382,    10,   235,   378,    12,    52,
      36,    12,    10,    17,    18,    19,   365,    13,    14,    23,
      24,   364,    26,    36,    20,   141,   441,   143,    45,   145,
      45,   147,   270,   271,   366,   367,    42,    61,    62,    63,
      64,     0,    42,    45,    82,    42,    36,    42,    39,    42,
      39,    78,    46,    82,    52,    65,    66,    67,    68,    69,
      70,    71,   477,    42,   479,    42,   481,   144,   483,   374,
     375,   376,    45,   583,    72,    45,    13,    55,    56,    57,
      58,    59,    60,    45,    78,   108,   109,    45,    42,    45,
      36,    94,    60,   508,    47,   510,    36,    47,   136,   206,
      36,    78,    95,    47,    95,    95,    95,   136,   137,    78,
      78,    57,    36,    82,    43,   113,    95,   143,   144,   117,
     118,    57,    42,    44,    47,   635,   143,   144,   143,   144,
     143,   144,   135,    57,   177,   130,   131,   143,   144,    14,
      43,   143,   144,   143,   144,    44,   143,   144,    43,   153,
      43,   155,   156,   157,   158,    58,   160,   161,   162,   163,
     161,   162,   166,   167,   168,   169,   170,   171,   164,   165,
     143,   144,    43,   143,   144,    95,   130,   131,    43,   177,
      43,   143,   144,   488,   489,   143,   144,   143,   144,   494,
     143,   144,   497,   143,   144,   500,    43,   175,   176,   143,
     144,   205,    36,   207,    36,   209,   207,    43,   209,   187,
     188,   189,   190,   209,   585,    82,   226,   227,   228,   229,
     143,   144,    58,    57,    78,    57,   144,   231,    82,   644,
     645,   130,   131,   108,   109,    76,    77,    78,    43,    36,
      43,    82,   247,   134,   135,   474,    43,   138,    87,   247,
     246,    90,    91,    92,    43,   253,   254,   255,   256,   257,
     258,   259,   260,   261,   106,   643,   270,   271,   110,    43,
     134,   135,   621,   269,   138,   106,    43,   620,    43,   110,
     284,   134,   520,   521,   288,   138,    43,   461,    78,   463,
     622,   623,    82,   143,   144,   136,   137,   130,   131,   275,
     407,   277,    43,   279,    43,   281,     0,     1,   122,   123,
     124,   125,   126,   127,   430,   431,   432,   433,   434,    13,
      43,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
      34,    35,   220,   221,   222,   223,   224,   225,   104,   105,
     106,   107,    46,    90,    91,    92,    43,     1,    44,     3,
       4,   365,   366,   367,    43,   369,   136,   137,   369,   485,
     486,   487,   368,   547,   370,   549,    20,    21,   382,   139,
     254,   255,   256,   379,    78,   381,    93,    94,    32,   505,
     133,   507,   211,   212,   213,   456,   457,   458,   136,   137,
     132,     1,    43,     3,     4,    89,    50,    51,    52,   144,
      54,    55,    56,    13,   412,   411,    82,   413,   414,   139,
      20,    21,   232,   233,   234,    93,    94,   130,   131,   257,
     258,    36,    32,   214,   215,   439,   440,    36,   462,   443,
     464,    36,   446,   260,   261,   449,   140,   141,   452,   453,
      50,    51,    52,    36,    54,    55,    56,   216,   217,   447,
     448,   624,   625,    36,   144,    42,   144,   471,    48,    47,
     471,     0,     1,    75,    82,    82,   472,   455,   456,   457,
     458,   459,   460,   461,    13,   463,    15,    16,    17,    18,
      19,    20,    21,    22,    23,    24,    25,    26,    27,    28,
      29,    30,    31,    32,    33,    34,    35,    82,    82,    44,
     506,    82,    82,     0,     1,   143,   520,   521,    44,   144,
      38,   144,   144,    78,   636,    42,    13,   523,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    78,
      42,    95,    95,    43,    42,    95,    42,    42,    95,    95,
      42,    95,   674,    95,    42,    95,    42,   572,    95,   547,
      89,   549,   577,    95,   572,   580,    42,    41,   583,   577,
      95,    95,   580,    95,    47,   583,   702,    41,    47,    78,
      43,    78,    41,    41,    78,    78,    95,    78,   602,    95,
      36,    78,    82,    82,    36,   615,   616,   617,   618,    82,
      82,    41,    41,    41,    38,    42,    78,   621,   622,   623,
      95,   625,    42,    42,   625,    42,    42,    41,    41,    41,
      41,    41,    41,    41,    95,    95,    43,    43,   636,   643,
      41,    41,   647,    41,    41,    41,   642,   144,   652,   647,
     646,    36,    41,    36,    36,    36,    82,    36,    42,   663,
      36,    36,   663,   668,   669,     0,     1,    41,    38,    42,
     668,   669,    43,    36,   678,    42,   674,   678,    13,    12,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,   699,    95,   707,    95,    41,   707,    40,    38,    41,
      43,    45,   716,    46,    45,   716,    49,    36,    36,   715,
     153,   443,   230,   218,   460,    58,    59,    60,    61,    62,
      63,    64,    65,    66,    67,    68,    69,    70,    71,    72,
      73,    74,   210,    76,    77,    78,    79,    80,    81,    82,
      83,    84,    85,    86,   259,    88,    52,   459,     4,   407,
       7,   219,    14,   678,   497,   236,   500,   494,    -1,   708,
     491,    -1,   707,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    40,    -1,
      -1,    43,    -1,    -1,    46,    -1,    -1,    49,    -1,    -1,
      -1,    -1,    -1,   136,   137,    -1,    -1,    -1,   141,    61,
      62,    63,    64,    65,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    -1,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    86,    -1,    88,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    96,    97,    98,    99,   100,   101,
     102,   103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   111,
     112,   113,   114,   115,   116,   117,   118,   119,   120,   121,
      14,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   136,   137,    -1,    -1,    -1,   141,
      -1,    -1,    -1,    -1,    -1,    -1,    40,    -1,    -1,    43,
      -1,    -1,    46,    -1,    -1,    49,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    -1,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,    86,    -1,    88,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    96,    97,    98,    99,   100,   101,   102,   103,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   111,   112,   113,
     114,   115,   116,   117,   118,   119,   120,   121,    14,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   136,   137,    -1,    -1,    -1,   141,    -1,    -1,
      -1,    -1,    -1,    -1,    40,    -1,    -1,    43,    -1,    -1,
      46,    -1,    -1,    49,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    -1,
      76,    77,    78,    79,    80,    81,    82,    83,    84,    85,
      86,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      96,    97,    98,    99,   100,   101,   102,   103,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   111,   112,   113,   114,   115,
     116,   117,   118,   119,   120,   121,    14,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     136,   137,    -1,    -1,    -1,   141,    -1,    -1,    -1,    -1,
      -1,    -1,    40,    -1,    -1,    43,    -1,    -1,    46,    -1,
      -1,    49,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    -1,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    -1,
      88,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    96,    97,
      98,    99,   100,   101,   102,   103,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   111,   112,   113,   114,   115,   116,   117,
     118,   119,   120,   121,    40,    -1,    -1,    43,    -1,    -1,
      46,    -1,    -1,    49,    -1,    -1,    -1,    -1,   136,   137,
      -1,    -1,    -1,   141,    -1,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    -1,
      76,    77,    78,    79,    80,    81,    82,    83,    84,    85,
      86,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      96,    97,    98,    99,   100,   101,   102,   103,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   111,   112,   113,   114,   115,
     116,   117,   118,   119,   120,   121,    -1,    -1,    40,    -1,
      -1,    43,    -1,    -1,    46,    -1,    -1,    49,    -1,    -1,
     136,   137,    -1,    -1,    -1,   141,    -1,    -1,   144,    61,
      62,    63,    64,    65,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    -1,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    86,    -1,    88,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    96,    97,    98,    99,   100,   101,
     102,   103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   111,
     112,   113,   114,   115,   116,   117,   118,   119,   120,   121,
      -1,    -1,    40,    -1,    -1,    43,    -1,    -1,    46,    -1,
      -1,    49,    -1,    -1,   136,   137,    -1,    -1,    -1,   141,
      -1,    -1,   144,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    -1,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    -1,
      88,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    96,    97,
      98,    99,   100,   101,   102,   103,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   111,   112,   113,   114,   115,   116,   117,
     118,   119,   120,   121,    -1,    -1,    40,    -1,    -1,    43,
      -1,    -1,    46,    -1,    -1,    49,    -1,    -1,   136,   137,
      -1,    -1,    -1,   141,    -1,    -1,   144,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    -1,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,    86,    -1,    88,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    96,    97,    98,    99,   100,   101,   102,   103,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   111,   112,   113,
     114,   115,   116,   117,   118,   119,   120,   121,    -1,    -1,
      40,    -1,    -1,    43,    -1,    -1,    46,    -1,    -1,    49,
      -1,    -1,   136,   137,    -1,    -1,    -1,   141,    -1,    -1,
     144,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    -1,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    -1,    88,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    96,    97,    98,    99,
     100,   101,   102,   103,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   111,   112,   113,   114,   115,   116,   117,   118,   119,
     120,   121,    38,    -1,    -1,    -1,    -1,    43,    -1,    -1,
      46,    -1,    -1,    49,    -1,    -1,   136,   137,    -1,    -1,
      -1,   141,    58,    -1,   144,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    -1,
      76,    77,    78,    79,    80,    81,    82,    83,    84,    85,
      86,    40,    88,    42,    43,    -1,    -1,    46,    -1,    -1,
      49,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,    -1,    76,    77,    78,
      79,    80,    81,    82,    83,    84,    85,    86,    -1,    88,
     136,   137,    -1,    -1,    -1,   141,    -1,    96,    97,    98,
      99,   100,   101,   102,   103,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   111,   112,   113,   114,   115,   116,   117,   118,
     119,   120,   121,    40,    -1,    -1,    43,    -1,    -1,    46,
      -1,    -1,    49,    -1,    -1,    -1,    -1,   136,   137,    -1,
      -1,    -1,   141,    -1,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,    -1,    76,
      77,    78,    79,    80,    81,    82,    83,    84,    85,    86,
      -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    96,
      97,    98,    99,   100,   101,   102,   103,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   111,   112,   113,   114,   115,   116,
     117,   118,   119,   120,   121,    40,    -1,    -1,    43,    -1,
      -1,    46,    -1,    -1,    49,    -1,    -1,    -1,    -1,   136,
     137,    -1,    -1,    -1,   141,    -1,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      -1,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    96,    97,    98,    99,   100,   101,   102,   103,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   111,   112,   113,   114,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    40,
      -1,    -1,    43,    -1,    -1,    46,    -1,    -1,    49,    -1,
      -1,   136,   137,    -1,    -1,    -1,   141,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    -1,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    40,    88,    -1,    43,
      -1,    -1,    46,    -1,    -1,    49,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    58,    59,    60,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    -1,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,    86,    -1,    88,   136,   137,    -1,    -1,    -1,
     141,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    40,    -1,    -1,
      43,    -1,    -1,    46,    -1,    -1,    49,    -1,    -1,    -1,
      -1,    -1,   136,   137,    -1,    -1,    -1,   141,    61,    62,
      63,    64,    65,    66,    67,    68,    69,    70,    71,    72,
      73,    74,    -1,    76,    77,    78,    79,    80,    81,    82,
      83,    84,    85,    86,    -1,    88,    43,    -1,    -1,    46,
      -1,    -1,    49,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,    -1,    76,
      77,    78,    79,    80,    81,    82,    83,    84,    85,    86,
      -1,    88,    -1,   136,   137,    -1,    -1,    -1,   141,    96,
      97,    98,    99,   100,   101,   102,   103,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   111,   112,   113,   114,   115,   116,
     117,   118,   119,   120,   121,    -1,    -1,    43,    -1,    -1,
      46,    -1,    -1,    49,    -1,    -1,    -1,    -1,    -1,   136,
     137,    -1,    -1,    -1,   141,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    -1,
      76,    77,    78,    79,    80,    81,    82,    83,    84,    85,
      86,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      96,    97,    98,    99,   100,   101,   102,   103,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   111,   112,   113,   114,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    43,    -1,
      -1,    46,    -1,    -1,    49,    -1,    -1,    -1,    -1,    -1,
     136,   137,    -1,    -1,    -1,   141,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      -1,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    43,    88,    -1,    46,    -1,    -1,    49,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    -1,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    -1,    88,     0,     1,
      -1,   136,   137,    -1,    -1,    -1,   141,    -1,    -1,    -1,
      -1,    13,    -1,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,     0,     1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   136,   137,    -1,    -1,    13,
     141,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
      34,    35,     0,     1,    -1,    -1,    78,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    13,    -1,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    26,    27,
      28,    29,    30,    31,    32,    33,    34,    35,     0,     1,
      -1,    -1,    -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    13,    -1,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,
      78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    78
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint16 yystos[] =
{
       0,   258,   259,   260,   261,     0,    13,   202,   203,     1,
       3,     4,    20,    21,    32,    50,    51,    52,    54,    55,
      56,   254,   255,    40,    43,    46,    49,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    88,    96,    97,    98,    99,   100,   101,   102,
     103,   111,   112,   113,   114,   115,   116,   117,   118,   119,
     120,   121,   136,   137,   141,   146,   147,   148,   149,   150,
     151,   152,   154,   155,   156,   157,   162,   164,   166,   168,
     169,   171,   172,   173,   174,   175,   181,   182,   183,   184,
     185,   186,   187,   188,   189,   193,    78,   204,   203,    36,
      40,    58,    59,    60,    73,    74,    82,    88,   136,   137,
     153,   157,   161,   163,   165,   167,   195,   189,   190,   189,
     191,   190,   190,    46,    78,   253,   108,   109,   194,   245,
     189,   192,   241,   193,   243,   191,   239,   190,   257,   170,
     189,   189,   159,   160,   189,    43,    43,    43,    43,    43,
      43,    43,    43,    43,    43,    43,    43,    43,    43,    43,
      43,    43,   157,   175,   182,   144,   144,    88,   174,   174,
     174,   174,   174,   174,    82,   136,   137,   152,   152,   152,
     152,   144,   181,   144,   181,   181,   144,   181,   144,   181,
     181,   181,    82,   157,    82,    43,    44,    43,   143,   144,
     139,   134,   135,   138,   136,   137,   130,   131,   133,   132,
     122,   123,   124,   125,   126,   127,   104,   105,   106,   107,
      89,    87,    90,    91,    92,    93,    94,    43,   206,    76,
      77,    78,   147,   197,   198,   199,   144,    38,    58,   153,
      58,    58,    82,   139,   134,   135,   138,   136,   137,    44,
     130,   131,    36,    36,    36,    36,    36,    36,   143,   144,
     144,   144,    36,    57,   251,    57,   251,    57,   251,    57,
     251,    57,   251,    39,    95,    42,    48,   159,    47,   189,
     189,   189,   189,    75,   158,   189,   191,   191,   189,   190,
     190,   189,   189,   189,   189,   189,   189,   174,   176,   177,
     178,   179,   180,   180,    82,    82,   174,   174,   174,   174,
      82,    82,    82,    82,   189,   147,   191,   201,    78,    82,
     189,   190,   191,   155,   162,   162,   162,   164,   164,   166,
     166,   169,   171,   172,   172,   172,   172,   172,   172,   181,
     181,   181,   181,   183,   189,   184,   184,   184,   186,   188,
      42,    78,   205,     1,    15,    16,    17,    18,    19,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,   207,   208,   209,   210,   211,
     222,   225,   230,   233,   234,   235,   236,   237,   238,   240,
     242,   244,   246,   247,   248,   250,    39,    95,   143,   190,
     195,   144,    38,   144,   144,   157,   161,   161,   161,   163,
     163,   167,   165,   165,    78,    82,   190,   192,   192,    78,
     256,   256,   256,   256,   256,   189,   189,    42,    42,    95,
      95,    43,    42,    95,    42,    42,    95,    95,    95,    95,
      42,    42,    95,    95,    42,    89,    90,    91,    92,    93,
      94,   106,   110,   106,   110,    95,    95,    95,    95,    42,
      42,    95,    47,    41,    47,    42,    95,    14,   245,    14,
     243,    14,   241,    14,   241,   190,   191,   190,   226,   223,
      78,   215,   219,   252,   214,   218,   252,   213,   217,   252,
     212,   216,   252,   199,   249,   190,    43,   190,    14,   239,
     231,    78,   198,    78,    41,   190,   195,   190,   190,    41,
      95,    95,   143,   144,   251,   251,   251,   251,   251,    36,
     189,   189,   253,   158,   189,   168,   168,   189,   189,   189,
     174,   176,   176,   176,   177,   179,   180,   152,   180,   152,
      82,    82,    82,    82,   191,   190,   186,    78,   253,   253,
     253,   253,   251,   251,   251,     1,   252,     1,   224,   252,
       1,   219,    47,   143,   144,     1,   218,    47,     1,   217,
      47,     1,   216,    47,    36,    95,   251,   190,   251,   253,
       1,   140,   141,   232,   253,    41,    41,    41,   192,   192,
      78,   190,    95,    42,    42,    42,    42,    42,    42,    42,
      42,    41,   180,    41,   180,    41,    41,    41,    41,    41,
      45,    45,    45,    45,    45,    45,   195,   220,   221,    78,
      82,    82,   136,   195,   195,    12,    60,    78,   195,   196,
     200,   199,    95,    45,    43,    43,    45,    38,    41,    41,
      41,   189,    95,    41,    41,   181,   181,   181,   181,   245,
     243,   241,   241,   144,   227,   191,   227,    36,    94,   135,
      41,    82,    36,    36,    60,    78,   200,   153,    43,    36,
     190,   239,   253,   253,   190,   195,    42,   189,   191,   227,
     228,   229,    36,    36,    36,   195,   195,    41,   153,    38,
      42,   201,    42,    42,    42,    36,    42,    95,    95,    41,
      41,    38,   200,    42,   251,    45,    45,   229,   228,   190,
     191,    36,    36
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  */

#define YYFAIL		goto yyerrlab

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yychar == YYEMPTY && yylen == 1)				\
    {								\
      yychar = (Token);						\
      yylval = (Value);						\
      yytoken = YYTRANSLATE (yychar);				\
      YYPOPSTACK (1);						\
      goto yybackup;						\
    }								\
  else								\
    {								\
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
#  define YY_LOCATION_PRINT(File, Loc)			\
     fprintf (File, "%d.%d-%d.%d",			\
	      (Loc).first_line, (Loc).first_column,	\
	      (Loc).last_line,  (Loc).last_column)
# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yylex (YYLEX_PARAM)
#else
# define YYLEX yylex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *bottom, yytype_int16 *top)
#else
static void
yy_stack_print (bottom, top)
    yytype_int16 *bottom;
    yytype_int16 *top;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; bottom <= top; ++bottom)
    YYFPRINTF (stderr, " %d", *bottom);
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule)
#else
static void
yy_reduce_print (yyvsp, yyrule)
    YYSTYPE *yyvsp;
    int yyrule;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      fprintf (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       );
      fprintf (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif



#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into YYRESULT an error message about the unexpected token
   YYCHAR while in state YYSTATE.  Return the number of bytes copied,
   including the terminating null byte.  If YYRESULT is null, do not
   copy anything; just return the number of bytes that would be
   copied.  As a special case, return 0 if an ordinary "syntax error"
   message will do.  Return YYSIZE_MAXIMUM if overflow occurs during
   size calculation.  */
static YYSIZE_T
yysyntax_error (char *yyresult, int yystate, int yychar)
{
  int yyn = yypact[yystate];

  if (! (YYPACT_NINF < yyn && yyn <= YYLAST))
    return 0;
  else
    {
      int yytype = YYTRANSLATE (yychar);
      YYSIZE_T yysize0 = yytnamerr (0, yytname[yytype]);
      YYSIZE_T yysize = yysize0;
      YYSIZE_T yysize1;
      int yysize_overflow = 0;
      enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
      char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
      int yyx;

# if 0
      /* This is so xgettext sees the translatable formats that are
	 constructed on the fly.  */
      YY_("syntax error, unexpected %s");
      YY_("syntax error, unexpected %s, expecting %s");
      YY_("syntax error, unexpected %s, expecting %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s");
# endif
      char *yyfmt;
      char const *yyf;
      static char const yyunexpected[] = "syntax error, unexpected %s";
      static char const yyexpecting[] = ", expecting %s";
      static char const yyor[] = " or %s";
      char yyformat[sizeof yyunexpected
		    + sizeof yyexpecting - 1
		    + ((YYERROR_VERBOSE_ARGS_MAXIMUM - 2)
		       * (sizeof yyor - 1))];
      char const *yyprefix = yyexpecting;

      /* Start YYX at -YYN if negative to avoid negative indexes in
	 YYCHECK.  */
      int yyxbegin = yyn < 0 ? -yyn : 0;

      /* Stay within bounds of both yycheck and yytname.  */
      int yychecklim = YYLAST - yyn + 1;
      int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
      int yycount = 1;

      yyarg[0] = yytname[yytype];
      yyfmt = yystpcpy (yyformat, yyunexpected);

      for (yyx = yyxbegin; yyx < yyxend; ++yyx)
	if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR)
	  {
	    if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
	      {
		yycount = 1;
		yysize = yysize0;
		yyformat[sizeof yyunexpected - 1] = '\0';
		break;
	      }
	    yyarg[yycount++] = yytname[yyx];
	    yysize1 = yysize + yytnamerr (0, yytname[yyx]);
	    yysize_overflow |= (yysize1 < yysize);
	    yysize = yysize1;
	    yyfmt = yystpcpy (yyfmt, yyprefix);
	    yyprefix = yyor;
	  }

      yyf = YY_(yyformat);
      yysize1 = yysize + yystrlen (yyf);
      yysize_overflow |= (yysize1 < yysize);
      yysize = yysize1;

      if (yysize_overflow)
	return YYSIZE_MAXIMUM;

      if (yyresult)
	{
	  /* Avoid sprintf, as that infringes on the user's name space.
	     Don't have undefined behavior even if the translation
	     produced a string with the wrong number of "%s"s.  */
	  char *yyp = yyresult;
	  int yyi = 0;
	  while ((*yyp = *yyf) != '\0')
	    {
	      if (*yyp == '%' && yyf[1] == 's' && yyi < yycount)
		{
		  yyp += yytnamerr (yyp, yyarg[yyi++]);
		  yyf += 2;
		}
	      else
		{
		  yyp++;
		  yyf++;
		}
	    }
	}
      return yysize;
    }
}
#endif /* YYERROR_VERBOSE */


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
#else
static void
yydestruct (yymsg, yytype, yyvaluep)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
#endif
{
  YYUSE (yyvaluep);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
	break;
    }
}


/* Prevent warnings from -Wmissing-prototypes.  */

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */



/* The look-ahead symbol.  */
int yychar;

/* The semantic value of the look-ahead symbol.  */
YYSTYPE yylval;

/* Number of syntax errors so far.  */
int yynerrs;



/*----------.
| yyparse.  |
`----------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void)
#else
int
yyparse ()

#endif
#endif
{
  
  int yystate;
  int yyn;
  int yyresult;
  /* Number of tokens to shift before error messages enabled.  */
  int yyerrstatus;
  /* Look-ahead token as an internal (translated) token number.  */
  int yytoken = 0;
#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

  /* Three stacks and their tools:
     `yyss': related to states,
     `yyvs': related to semantic values,
     `yyls': related to locations.

     Refer to the stacks thru separate pointers, to allow yyoverflow
     to reallocate them elsewhere.  */

  /* The state stack.  */
  yytype_int16 yyssa[YYINITDEPTH];
  yytype_int16 *yyss = yyssa;
  yytype_int16 *yyssp;

  /* The semantic value stack.  */
  YYSTYPE yyvsa[YYINITDEPTH];
  YYSTYPE *yyvs = yyvsa;
  YYSTYPE *yyvsp;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  YYSIZE_T yystacksize = YYINITDEPTH;

  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;


  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY;		/* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */

  yyssp = yyss;
  yyvsp = yyvs;

  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;


	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),

		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss);
	YYSTACK_RELOCATE (yyvs);

#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;


      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     look-ahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to look-ahead token.  */
  yyn = yypact[yystate];
  if (yyn == YYPACT_NINF)
    goto yydefault;

  /* Not known => get a look-ahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid look-ahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yyn == 0 || yyn == YYTABLE_NINF)
	goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the look-ahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token unless it is eof.  */
  if (yychar != YYEOF)
    yychar = YYEMPTY;

  yystate = yyn;
  *++yyvsp = yylval;

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 3:
#line 253 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(2) - (2)].node); ;}
    break;

  case 5:
#line 257 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(2) - (2)].node); ;}
    break;

  case 6:
#line 259 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {node_int_setcar((yyvsp[(2) - (2)].node), -(node_get_int((yyvsp[(2) - (2)].node)))); (yyval.node) = (yyvsp[(2) - (2)].node);;}
    break;

  case 11:
#line 272 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, TWODOTS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));;}
    break;

  case 12:
#line 276 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, TWODOTS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));;}
    break;

  case 15:
#line 282 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, UWCONST, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 16:
#line 284 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SWCONST, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 17:
#line 286 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, WSIZEOF, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); ;}
    break;

  case 18:
#line 288 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, CAST_TOINT, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); ;}
    break;

  case 21:
#line 292 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                 nusmv_yyerror("fractional constants are not supported.");
                 YYABORT;
               ;}
    break;

  case 22:
#line 297 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                 nusmv_yyerror("exponential constants are not supported.");
                 YYABORT;
               ;}
    break;

  case 23:
#line 302 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                 nusmv_yyerror("real constants are not supported.");
                 YYABORT;
               ;}
    break;

  case 25:
#line 311 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                 nusmv_yyerror("functions are not supported.");
                 YYABORT;
               ;}
    break;

  case 26:
#line 318 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                    int ntype = node_get_type((yyvsp[(1) - (4)].node));
                    if (ATOM != ntype && DOT != ntype && SELF != ntype) {
                      nusmv_yyerror_lined("incorrect DOT expression", (yyvsp[(2) - (4)].lineno));
                      YYABORT;
                    }
                (yyval.node) = new_lined_node(NODEMGR, NFUNCTION, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));
               ;}
    break;

  case 28:
#line 338 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, UMINUS, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 30:
#line 340 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, SELF,Nil,Nil);;}
    break;

  case 31:
#line 342 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                    int ntype = node_get_type((yyvsp[(1) - (3)].node));
                    if (ATOM != ntype && DOT != ntype && ARRAY != ntype && SELF != ntype) {
                      nusmv_yyerror_lined("incorrect DOT expression", (yyvsp[(2) - (3)].lineno));
                      YYABORT;
                    }
                    (yyval.node) = new_lined_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)) ;
                  ;}
    break;

  case 32:
#line 351 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                   int ntype = node_get_type((yyvsp[(1) - (3)].node));
                   if (ATOM != ntype && DOT != ntype && ARRAY != ntype && SELF != ntype) {
                     nusmv_yyerror_lined("incorrect DOT expression", (yyvsp[(2) - (3)].lineno));
                     YYABORT;
                   }
                   (yyval.node) = new_lined_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)) ;
                  ;}
    break;

  case 33:
#line 360 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                   /* array may have any expression on the left.
                      The type check will detect any problems */
                   (yyval.node) = new_lined_node(NODEMGR, ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));
                  ;}
    break;

  case 34:
#line 366 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                    (yyval.node) = new_lined_node(NODEMGR, BIT_SELECTION, (yyvsp[(1) - (6)].node),
                                        new_lined_node(NODEMGR, COLON, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(4) - (6)].lineno)), (yyvsp[(2) - (6)].lineno));
                  ;}
    break;

  case 35:
#line 370 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); ;}
    break;

  case 36:
#line 371 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { /* abs(a) := (a >= 0) ? a : - a */
                                                      node_ptr zero = new_lined_node(NODEMGR, NUMBER, NODE_FROM_INT((int)(0)), Nil, (yyvsp[(1) - (4)].lineno));
                                                      node_ptr cond = new_lined_node(NODEMGR, GE, (yyvsp[(3) - (4)].node), zero, (yyvsp[(1) - (4)].lineno));
                                                      node_ptr minus_a = new_lined_node(NODEMGR, UMINUS, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno));
                                                      (yyval.node) = new_lined_node(NODEMGR, IFTHENELSE, new_lined_node(NODEMGR, COLON, cond, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].lineno)), minus_a, (yyvsp[(1) - (4)].lineno)); ; ;}
    break;

  case 37:
#line 376 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { /* MIN(a,b) := a < b ? a : b */
                                                                           node_ptr cond = new_lined_node(NODEMGR, LT, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno));
                                                                           (yyval.node) = new_lined_node(NODEMGR, IFTHENELSE, new_lined_node(NODEMGR, COLON, cond, (yyvsp[(3) - (6)].node), (yyvsp[(1) - (6)].lineno)), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ; ;}
    break;

  case 38:
#line 379 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { /* MAX(a,b) := a < b ? b : a */
                                                                           node_ptr cond = new_lined_node(NODEMGR, LT, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno));
                                                                           (yyval.node) = new_lined_node(NODEMGR, IFTHENELSE, new_lined_node(NODEMGR, COLON, cond, (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)), (yyvsp[(3) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;;}
    break;

  case 39:
#line 382 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, NOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 40:
#line 383 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, CAST_BOOL, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); ;}
    break;

  case 41:
#line 384 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, CAST_WORD1, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); ;}
    break;

  case 42:
#line 385 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, NEXT, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); ;}
    break;

  case 43:
#line 386 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, CAST_SIGNED, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); ;}
    break;

  case 44:
#line 387 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, CAST_UNSIGNED, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); ;}
    break;

  case 45:
#line 388 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EXTEND, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 46:
#line 389 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, WRESIZE, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 47:
#line 390 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); ;}
    break;

  case 48:
#line 394 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, WAREAD, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 49:
#line 397 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, WAWRITE, (yyvsp[(3) - (8)].node), new_node(NODEMGR, WAWRITE, (yyvsp[(5) - (8)].node), (yyvsp[(7) - (8)].node)), (yyvsp[(2) - (8)].lineno)); ;}
    break;

  case 50:
#line 399 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, CONST_ARRAY, new_node(NODEMGR, TYPEOF, (yyvsp[(5) - (9)].node), Nil), (yyvsp[(8) - (9)].node), (yyvsp[(1) - (9)].lineno)); ;}
    break;

  case 51:
#line 401 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, COUNT, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(2) - (4)].lineno));;}
    break;

  case 52:
#line 405 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil); ;}
    break;

  case 53:
#line 406 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = cons(NODEMGR, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); ;}
    break;

  case 54:
#line 411 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
               const ErrorMgr_ptr errmgr =
                 ERROR_MGR(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_ERROR_MANAGER));
               node_ptr fail =
                 ErrorMgr_failure_make(errmgr,
                                       "case conditions are not exhaustive",
                                       FAILURE_CASE_NOT_EXHAUSTIVE,
                                       nusmv_yylineno);
               (yyval.node) = new_node(NODEMGR, CASE, (yyvsp[(1) - (1)].node), fail);
             ;}
    break;

  case 55:
#line 421 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_node(NODEMGR, CASE, (yyvsp[(1) - (2)].node), (yyvsp[(2) - (2)].node)); ;}
    break;

  case 56:
#line 426 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = build_case_colon_node((yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno)); ;}
    break;

  case 58:
#line 432 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, CONCATENATION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 60:
#line 438 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, CONCATENATION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 62:
#line 444 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, TIMES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 63:
#line 445 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, DIVIDE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 64:
#line 446 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, MOD, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 66:
#line 451 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, TIMES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 67:
#line 452 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, DIVIDE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 68:
#line 453 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, MOD, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 70:
#line 459 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, PLUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 71:
#line 460 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, MINUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 73:
#line 466 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, PLUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 74:
#line 467 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, MINUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 76:
#line 471 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, LSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 77:
#line 472 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, RSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 79:
#line 476 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, LSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 80:
#line 477 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, RSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 83:
#line 485 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); ;}
    break;

  case 85:
#line 489 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, UNION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));;}
    break;

  case 87:
#line 494 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, UNION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 89:
#line 498 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, SETIN, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 91:
#line 503 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EQUAL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 92:
#line 504 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, NOTEQUAL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 93:
#line 505 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, LT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 94:
#line 506 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, GT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 95:
#line 507 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, LE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 96:
#line 508 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, GE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 99:
#line 516 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EX, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 100:
#line 517 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, AX, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 101:
#line 518 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EF, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 102:
#line 519 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, AF, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 103:
#line 520 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EG, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 104:
#line 521 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, AG, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 105:
#line 523 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, AU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 106:
#line 525 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 107:
#line 527 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, ABU, new_lined_node(NODEMGR, AU, (yyvsp[(3) - (7)].node), (yyvsp[(6) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)); ;}
    break;

  case 108:
#line 529 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EBU, new_lined_node(NODEMGR, EU, (yyvsp[(3) - (7)].node), (yyvsp[(6) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)); ;}
    break;

  case 109:
#line 530 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EBF, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); ;}
    break;

  case 110:
#line 531 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, ABF, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); ;}
    break;

  case 111:
#line 532 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EBG, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); ;}
    break;

  case 112:
#line 533 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, ABG, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); ;}
    break;

  case 113:
#line 536 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, NOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 115:
#line 543 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, AND, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 117:
#line 547 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, OR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 118:
#line 548 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, XOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 119:
#line 549 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, XNOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 121:
#line 553 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, IFF, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 123:
#line 558 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, IMPLIES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 127:
#line 571 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_NEXT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 128:
#line 572 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_PREC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 129:
#line 573 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_NOTPRECNOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 130:
#line 574 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_GLOBAL, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 131:
#line 576 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_GLOBAL, (yyvsp[(7) - (7)].node), new_lined_node(NODEMGR, TWODOTS, (yyvsp[(3) - (7)].node), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(1) - (7)].lineno));;}
    break;

  case 132:
#line 577 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_HISTORICAL, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 133:
#line 579 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_HISTORICAL, (yyvsp[(7) - (7)].node), new_lined_node(NODEMGR, TWODOTS, (yyvsp[(3) - (7)].node), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(1) - (7)].lineno));;}
    break;

  case 134:
#line 580 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_FUTURE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 135:
#line 582 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_FUTURE, (yyvsp[(7) - (7)].node), new_lined_node(NODEMGR, TWODOTS, (yyvsp[(3) - (7)].node), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(1) - (7)].lineno));;}
    break;

  case 136:
#line 583 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_ONCE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 137:
#line 585 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, OP_ONCE, (yyvsp[(7) - (7)].node), new_lined_node(NODEMGR, TWODOTS, (yyvsp[(3) - (7)].node), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(1) - (7)].lineno));;}
    break;

  case 138:
#line 587 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, NOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); ;}
    break;

  case 140:
#line 596 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, UNTIL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));;}
    break;

  case 141:
#line 598 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SINCE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));;}
    break;

  case 142:
#line 600 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, NOT,
                           new_lined_node(NODEMGR, UNTIL,
                             new_lined_node(NODEMGR, NOT, (yyvsp[(1) - (3)].node), Nil, node_get_lineno((yyvsp[(1) - (3)].node))),
                             new_lined_node(NODEMGR, NOT, (yyvsp[(3) - (3)].node), Nil, node_get_lineno((yyvsp[(3) - (3)].node))),
                             (yyvsp[(2) - (3)].lineno)), Nil, (yyvsp[(2) - (3)].lineno));
                  ;}
    break;

  case 143:
#line 607 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, NOT,
                          new_lined_node(NODEMGR, SINCE,
                              new_lined_node(NODEMGR, NOT, (yyvsp[(1) - (3)].node), Nil, node_get_lineno((yyvsp[(1) - (3)].node))),
                              new_lined_node(NODEMGR, NOT, (yyvsp[(3) - (3)].node), Nil, node_get_lineno((yyvsp[(3) - (3)].node))),
                              (yyvsp[(2) - (3)].lineno)), Nil, (yyvsp[(2) - (3)].lineno));
                  ;}
    break;

  case 145:
#line 617 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, AND, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 147:
#line 622 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, OR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 148:
#line 623 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, XOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 149:
#line 624 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, XNOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 151:
#line 629 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, IFTHENELSE, new_lined_node(NODEMGR, COLON, (yyvsp[(1) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(2) - (5)].lineno)), (yyvsp[(5) - (5)].node), (yyvsp[(2) - (5)].lineno)); ;}
    break;

  case 153:
#line 634 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, IFF, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 155:
#line 639 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, IMPLIES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); ;}
    break;

  case 157:
#line 650 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_SIMPLE)) YYABORT;;}
    break;

  case 158:
#line 653 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_NEXT)) YYABORT;;}
    break;

  case 159:
#line 656 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_CTL)) YYABORT;;}
    break;

  case 160:
#line 659 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_LTL)) YYABORT;;}
    break;

  case 161:
#line 664 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, MINU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 162:
#line 666 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, MAXU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); ;}
    break;

  case 163:
#line 674 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, BOOLEAN, Nil, Nil);;}
    break;

  case 164:
#line 676 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, UNSIGNED_WORD, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno));;}
    break;

  case 165:
#line 678 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, UNSIGNED_WORD, (yyvsp[(4) - (5)].node), Nil, (yyvsp[(1) - (5)].lineno));;}
    break;

  case 166:
#line 680 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SIGNED_WORD, (yyvsp[(4) - (5)].node), Nil, (yyvsp[(1) - (5)].lineno));;}
    break;

  case 168:
#line 683 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SCALAR, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 169:
#line 685 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, WORDARRAY_TYPE, (yyvsp[(4) - (7)].node), (yyvsp[(7) - (7)].node), (yyvsp[(1) - (7)].lineno));;}
    break;

  case 170:
#line 687 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, ARRAY_TYPE, (yyvsp[(2) - (4)].node), (yyvsp[(4) - (4)].node), (yyvsp[(1) - (4)].lineno));;}
    break;

  case 171:
#line 689 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {nusmv_yyerror("unbounded arrays are not supported.");
                   YYABORT;
                  ;}
    break;

  case 174:
#line 697 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, PROCESS, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 175:
#line 700 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, find_atom(NODEMGR, (yyvsp[(1) - (1)].node)), Nil); free_node(NODEMGR, (yyvsp[(1) - (1)].node));;}
    break;

  case 176:
#line 701 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, find_atom(NODEMGR, (yyvsp[(3) - (3)].node)), (yyvsp[(1) - (3)].node)); free_node(NODEMGR, (yyvsp[(3) - (3)].node));;}
    break;

  case 182:
#line 711 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));;}
    break;

  case 183:
#line 714 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, MODTYPE, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 184:
#line 715 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, MODTYPE, (yyvsp[(1) - (3)].node), Nil);;}
    break;

  case 185:
#line 717 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, MODTYPE, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), node_get_lineno((yyvsp[(1) - (4)].node)));;}
    break;

  case 186:
#line 719 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                    /* $$ = new_lined_node(NODEMGR, ARRAY, $2, $4, $1); */
                    /* array of modules is not supported any more.
                       NOTE: In future if there are some syntact conflicts
                       this case can be removed */
                    nusmv_yyerror_lined("array of modules is no supported", (yyvsp[(1) - (4)].lineno));
                    YYABORT;
                  ;}
    break;

  case 187:
#line 730 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node),Nil);;}
    break;

  case 188:
#line 731 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(3) - (3)].node), (yyvsp[(1) - (3)].node));;}
    break;

  case 189:
#line 743 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 190:
#line 744 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));;}
    break;

  case 191:
#line 748 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, MODULE, (yyvsp[(2) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(1) - (3)].lineno));;}
    break;

  case 192:
#line 750 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, MODTYPE, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 193:
#line 751 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, MODTYPE, (yyvsp[(1) - (3)].node), Nil);;}
    break;

  case 194:
#line 753 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, MODTYPE, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));;}
    break;

  case 195:
#line 755 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, find_atom(NODEMGR, (yyvsp[(1) - (1)].node)), Nil); free_node(NODEMGR, (yyvsp[(1) - (1)].node));;}
    break;

  case 196:
#line 756 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, find_atom(NODEMGR, (yyvsp[(3) - (3)].node)), (yyvsp[(1) - (3)].node)); free_node(NODEMGR, (yyvsp[(3) - (3)].node));;}
    break;

  case 197:
#line 761 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = Nil;;}
    break;

  case 198:
#line 762 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));;}
    break;

  case 199:
#line 763 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 220:
#line 794 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, VAR, Nil, Nil, (yyvsp[(1) - (1)].lineno));;}
    break;

  case 221:
#line 795 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, VAR, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 222:
#line 798 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, FROZENVAR, Nil, Nil, (yyvsp[(1) - (1)].lineno));;}
    break;

  case 223:
#line 799 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, FROZENVAR, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 224:
#line 802 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, IVAR, Nil, Nil, (yyvsp[(1) - (1)].lineno));;}
    break;

  case 225:
#line 803 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, IVAR, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 226:
#line 805 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                 nusmv_yyerror("functions definitions are not supported.");
                 YYABORT;
               ;}
    break;

  case 227:
#line 809 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                 nusmv_yyerror("functions definitions are not supported.");
                 YYABORT;
               ;}
    break;

  case 228:
#line 815 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 229:
#line 816 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));;}
    break;

  case 230:
#line 817 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 231:
#line 819 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 232:
#line 820 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));;}
    break;

  case 233:
#line 821 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 234:
#line 823 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 235:
#line 824 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));;}
    break;

  case 236:
#line 825 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 237:
#line 827 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 238:
#line 828 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));;}
    break;

  case 239:
#line 829 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 240:
#line 832 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));;}
    break;

  case 241:
#line 834 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));;}
    break;

  case 242:
#line 836 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));;}
    break;

  case 243:
#line 838 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));;}
    break;

  case 244:
#line 841 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, NFUNCTION_TYPE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 245:
#line 845 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil); ;}
    break;

  case 246:
#line 846 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = cons(NODEMGR, (yyvsp[(3) - (3)].node), (yyvsp[(1) - (3)].node)); ;}
    break;

  case 247:
#line 851 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, DEFINE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 248:
#line 853 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = Nil;;}
    break;

  case 249:
#line 854 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));;}
    break;

  case 250:
#line 855 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 251:
#line 859 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, EQDEF, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));;}
    break;

  case 252:
#line 861 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, EQDEF, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));
                                 /* Note that array-define is declared
                                    as normal define.
                                    Then compile_instantiate in compileFlatten.c
                                    distinguish them by detecting
                                    ARRAY_DEF on right hand side.
                                   */
                                 ;}
    break;

  case 253:
#line 873 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, DEFINE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 254:
#line 877 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = Nil;;}
    break;

  case 255:
#line 878 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, new_lined_node(NODEMGR, EQDEF, (yyvsp[(2) - (5)].node), (yyvsp[(4) - (5)].node), (yyvsp[(3) - (5)].lineno)), (yyvsp[(1) - (5)].node));;}
    break;

  case 256:
#line 879 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 257:
#line 883 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) =  new_lined_node(NODEMGR, ARRAY_DEF, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 258:
#line 884 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) =  new_lined_node(NODEMGR, ARRAY_DEF, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 259:
#line 888 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 260:
#line 889 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 261:
#line 893 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 262:
#line 894 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node),Nil);;}
    break;

  case 263:
#line 898 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, ASSIGN, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 264:
#line 900 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = Nil;;}
    break;

  case 265:
#line 901 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, AND, (yyvsp[(1) - (2)].node), (yyvsp[(2) - (2)].node));;}
    break;

  case 266:
#line 902 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); ;}
    break;

  case 267:
#line 905 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, EQDEF, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));;}
    break;

  case 268:
#line 907 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EQDEF,
                                        new_lined_node(NODEMGR, SMALLINIT, (yyvsp[(3) - (7)].node), Nil, (yyvsp[(1) - (7)].lineno)),
                                        (yyvsp[(6) - (7)].node), (yyvsp[(5) - (7)].lineno));
                  ;}
    break;

  case 269:
#line 912 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = new_lined_node(NODEMGR, EQDEF,
                                        new_lined_node(NODEMGR, NEXT, (yyvsp[(3) - (7)].node), Nil, (yyvsp[(1) - (7)].lineno)),
                                        (yyvsp[(6) - (7)].node), (yyvsp[(5) - (7)].lineno));
                  ;}
    break;

  case 270:
#line 919 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, INIT, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 271:
#line 921 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, INVAR, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 272:
#line 923 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, TRANS, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 273:
#line 927 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, JUSTICE, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 274:
#line 930 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, JUSTICE, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 275:
#line 935 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COMPASSION, cons(NODEMGR, (yyvsp[(3) - (7)].node),(yyvsp[(5) - (7)].node)), Nil, (yyvsp[(1) - (7)].lineno));;}
    break;

  case 276:
#line 939 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); ;}
    break;

  case 277:
#line 940 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));;}
    break;

  case 278:
#line 942 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, INVARSPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 279:
#line 943 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, INVARSPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));;}
    break;

  case 280:
#line 946 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); ;}
    break;

  case 281:
#line 947 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));;}
    break;

  case 282:
#line 949 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 283:
#line 950 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 284:
#line 951 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));;}
    break;

  case 285:
#line 952 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));;}
    break;

  case 286:
#line 955 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); ;}
    break;

  case 287:
#line 956 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));;}
    break;

  case 288:
#line 959 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, LTLSPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 289:
#line 960 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, LTLSPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));;}
    break;

  case 290:
#line 963 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); ;}
    break;

  case 291:
#line 964 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));;}
    break;

  case 292:
#line 966 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COMPUTE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 293:
#line 967 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COMPUTE, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));;}
    break;

  case 294:
#line 972 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
  if (nusmv_parse_psl() != 0) {
    YYABORT;
  }
  (yyval.node) = new_lined_node(NODEMGR, PSLSPEC, psl_parsed_tree, psl_property_name, (yyvsp[(1) - (1)].lineno));
  psl_property_name = Nil;
;}
    break;

  case 295:
#line 982 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, CONSTANTS, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 296:
#line 986 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = Nil;;}
    break;

  case 297:
#line 987 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = cons(NODEMGR, (yyvsp[(1) - (1)].node), Nil);;}
    break;

  case 298:
#line 988 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = cons(NODEMGR, (yyvsp[(3) - (3)].node), (yyvsp[(1) - (3)].node));;}
    break;

  case 299:
#line 995 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, ISA, (yyvsp[(2) - (2)].node), Nil);;}
    break;

  case 301:
#line 999 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {;}
    break;

  case 303:
#line 1008 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 304:
#line 1009 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 305:
#line 1010 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));;}
    break;

  case 306:
#line 1012 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { node_ptr tmp = new_lined_node(NODEMGR, NUMBER,
                                                      PTR_FROM_INT(node_ptr, -node_get_int((yyvsp[(4) - (5)].node))),
                                                      Nil,
                                                      (yyvsp[(3) - (5)].lineno));
                        (yyval.node) = new_node(NODEMGR, ARRAY, (yyvsp[(1) - (5)].node), tmp);
                      ;}
    break;

  case 308:
#line 1021 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, SELF,Nil,Nil);;}
    break;

  case 309:
#line 1022 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 310:
#line 1023 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 311:
#line 1024 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));;}
    break;

  case 312:
#line 1031 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = (yyvsp[(1) - (1)].node);;}
    break;

  case 313:
#line 1032 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {return(1);;}
    break;

  case 314:
#line 1033 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {return(1);;}
    break;

  case 315:
#line 1037 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, INIT, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 316:
#line 1039 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, JUSTICE, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 317:
#line 1041 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, TRANS, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 318:
#line 1043 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, CONSTRAINT, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 319:
#line 1045 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, ITYPE, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 320:
#line 1048 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, SIMPWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 321:
#line 1049 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, NEXTWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 322:
#line 1050 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, CTLWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 323:
#line 1051 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, LTLWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 324:
#line 1052 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COMPWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));;}
    break;

  case 325:
#line 1053 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_lined_node(NODEMGR, COMPID, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));;}
    break;

  case 326:
#line 1057 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = find_atom(NODEMGR, (yyvsp[(1) - (1)].node)); free_node(NODEMGR, (yyvsp[(1) - (1)].node)); ;}
    break;

  case 327:
#line 1058 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = find_node(NODEMGR, DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));;}
    break;

  case 328:
#line 1059 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = find_node(NODEMGR, ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));;}
    break;

  case 329:
#line 1062 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); ;}
    break;

  case 330:
#line 1063 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {(yyval.node) = new_node(NODEMGR, CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));;}
    break;

  case 331:
#line 1069 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
  if (PARSE_MODULES != parse_mode_flag) {
    nusmv_yyerror("unexpected MODULE definition encountered during parsing");
    YYABORT;
  }
;}
    break;

  case 332:
#line 1076 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                  parsed_tree = (yyvsp[(2) - (2)].node);
                ;}
    break;

  case 333:
#line 1079 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                  if (PARSE_COMMAND != parse_mode_flag) {
                    nusmv_yyerror("unexpected command encountered during parsing");
                    YYABORT;
                  }
                ;}
    break;

  case 334:
#line 1085 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {parsed_tree = (yyvsp[(2) - (2)].node);;}
    break;

  case 335:
#line 1086 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {
                  if (PARSE_LTL_EXPR != parse_mode_flag){
                    nusmv_yyerror("unexpected expression encountered during parsing");
                    YYABORT;
                  }
                ;}
    break;

  case 336:
#line 1092 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
    {parsed_tree = (yyvsp[(2) - (2)].node);;}
    break;


/* Line 1267 of yacc.c.  */
#line 4185 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.c"
      default: break;
    }
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;


  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
      {
	YYSIZE_T yysize = yysyntax_error (0, yystate, yychar);
	if (yymsg_alloc < yysize && yymsg_alloc < YYSTACK_ALLOC_MAXIMUM)
	  {
	    YYSIZE_T yyalloc = 2 * yysize;
	    if (! (yysize <= yyalloc && yyalloc <= YYSTACK_ALLOC_MAXIMUM))
	      yyalloc = YYSTACK_ALLOC_MAXIMUM;
	    if (yymsg != yymsgbuf)
	      YYSTACK_FREE (yymsg);
	    yymsg = (char *) YYSTACK_ALLOC (yyalloc);
	    if (yymsg)
	      yymsg_alloc = yyalloc;
	    else
	      {
		yymsg = yymsgbuf;
		yymsg_alloc = sizeof yymsgbuf;
	      }
	  }

	if (0 < yysize && yysize <= yymsg_alloc)
	  {
	    (void) yysyntax_error (yymsg, yystate, yychar);
	    yyerror (yymsg);
	  }
	else
	  {
	    yyerror (YY_("syntax error"));
	    if (yysize != 0)
	      goto yyexhaustedlab;
	  }
      }
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse look-ahead token after an
	 error, discard it.  */

      if (yychar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yychar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yydestruct ("Error: discarding",
		      yytoken, &yylval);
	  yychar = YYEMPTY;
	}
    }

  /* Else will try to reuse look-ahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (yyn != YYPACT_NINF)
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
	    {
	      yyn = yytable[yyn];
	      if (0 < yyn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
	YYABORT;


      yydestruct ("Error: popping",
		  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  *++yyvsp = yylval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#ifndef yyoverflow
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEOF && yychar != YYEMPTY)
     yydestruct ("Cleanup: discarding lookahead",
		 yytoken, &yylval);
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}


#line 1095 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"

  /* BEGINS: grammar.y.3.50 */
/***************************************************************  -*-C-*-  ***/

/* Additional source code */

/* outputs the current token with the provided string and then may terminate */
void nusmv_yyerror(char *s)
{
  /* In the input.l file we explicity tell flex that we want a pointer
     (see man flex -> %pointer). So we don't need to check if nusmv_yytext
     is declared as pointer or as array  */
  extern char* nusmv_yytext;
  extern int nusmv_yylineno;
  const OptsHandler_ptr opmgr = GET_OPTS;
  const ErrorMgr_ptr errmgr =
    ERROR_MGR(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_ERROR_MANAGER));
  const StreamMgr_ptr streams =
    STREAM_MGR(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_STREAM_MANAGER));

  parser_add_syntax_error(__nusmv_parser_env__, get_input_file(opmgr), nusmv_yylineno, nusmv_yytext, s);
  if (!OptsHandler_get_bool_option_value(opmgr, OPT_PARSER_IS_LAX)) {
    ErrorMgr_start_parsing_err(errmgr);
    StreamMgr_print_error(streams,  "at token \"%s\": %s\n", nusmv_yytext, s);
    if (opt_batch(opmgr)) { ErrorMgr_finish_parsing_err(errmgr); }
  }
}

/* the same as yyerror, except at first it sets the line number and does
 not output the current token
*/
void nusmv_yyerror_lined(const char *s, int line)
{
  extern char* nusmv_yytext;
  extern int nusmv_yylineno;
  const OptsHandler_ptr opmgr = GET_OPTS;
  const ErrorMgr_ptr errmgr =
    ERROR_MGR(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_ERROR_MANAGER));
  const StreamMgr_ptr streams =
    STREAM_MGR(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_STREAM_MANAGER));

  /*set the line number */
  nusmv_yylineno = line;

  parser_add_syntax_error(__nusmv_parser_env__, get_input_file(opmgr), line, nusmv_yytext, s);
  if (!OptsHandler_get_bool_option_value(opmgr, OPT_PARSER_IS_LAX)) {
    ErrorMgr_start_parsing_err(errmgr);
    StreamMgr_print_error(streams,  ": %s\n", s);
    if (opt_batch(opmgr)) { ErrorMgr_finish_parsing_err(errmgr); }
  }
}

int nusmv_yywrap()
{
  return(1);
}


/* Given a node (possibly a relative or absolute context)
   constructs a node that is contextualized absolutely
   (i.e. relatively to main module). This is used to construct
   context of properties that have to be instatiated in main
   module */
static node_ptr node2maincontext(node_ptr node)
{
  node_ptr ctx;

  if (node_get_type(node) == CONTEXT) {
    /* already a context */
    ctx = CompileFlatten_concat_contexts(__nusmv_parser_env__, Nil, car(node));
    return find_node(NODEMGR, CONTEXT, ctx, cdr(node));
  }

  /* an atom, array or dot */
  return find_node(NODEMGR, CONTEXT, Nil, node);
}

/* This functions build the COLON node for case expressions.  If
   backward compatibility is enabled, and the condition expression is
   found to be the constant "1", then a warning is printed and the
   condition is replaced with TRUE. */
static node_ptr build_case_colon_node(node_ptr l,
                                      node_ptr r,
                                      int linum)
{
  const OptsHandler_ptr opts = GET_OPTS;
  const StreamMgr_ptr streams =
    STREAM_MGR(NuSMVEnv_get_value(__nusmv_parser_env__, ENV_STREAM_MANAGER));

  node_ptr res;

  static int user_warned = 0;

  if (opt_backward_comp(opts) &&
      (NUMBER == node_get_type(l)) && (1 == NODE_TO_INT(car(l)))) {

    /* Print this warning only once. */
    if (!user_warned) {
      StreamMgr_print_error(streams,
              "\nWARNING *** Option backward_compatibility (-old) is deprecate ***\n");
      StreamMgr_print_error(streams,
              "WARNING *** and will no longer be supported in future NuSMV versions. ***\n\n");
      user_warned = 1;
    }

    StreamMgr_print_error(streams,  "WARNING (");

    if (get_input_file(opts)) {
      StreamMgr_print_error(streams,  "file %s", get_input_file(opts));
    }
    else StreamMgr_print_error(streams,  "file stdin");

    StreamMgr_print_error(streams,
            ", line %d) : Deprecated use of \"1\" for case condition\n", linum);

    res = new_lined_node(NODEMGR, COLON, new_node(NODEMGR, TRUEEXP, Nil, Nil), r, linum);
  }
  else {
    res = new_lined_node(NODEMGR, COLON, l, r, linum);
  }

  return res;
}

/* this functions checks that the expression is formed syntactically correct.
   Takes the expression to be checked, the expected kind of the
   expression. Returns true if the expression is formed correctly, and
   false otherwise.
   See enum EXP_KIND for more info about syntactic well-formedness.
*/
static boolean isCorrectExp(node_ptr exp, enum EXP_KIND expectedKind)
{
  switch(node_get_type(exp))
    {
      /* atomic expression (or thier operands have been checked earlier) */
    case FAILURE:
    case FALSEEXP:
    case TRUEEXP:
    case NUMBER:
    case NUMBER_UNSIGNED_WORD:
    case NUMBER_SIGNED_WORD:
    case NUMBER_FRAC:
    case NUMBER_REAL:
    case NUMBER_EXP:
    case UWCONST:
    case SWCONST:
    case TWODOTS:
    case DOT:
    case ATOM:
    case SELF:
    case ARRAY:
    case COUNT:
      return true;

      /* unary operators incompatible with LTL and CTL operator */
    case CAST_BOOL:
    case CAST_WORD1:
    case CAST_SIGNED:
    case CAST_UNSIGNED:
    case WSIZEOF:
    case CAST_TOINT:
    case TYPEOF:
      if (EXP_CTL == expectedKind) {
        return isCorrectExp(car(exp), EXP_SIMPLE);
      }
      else if (EXP_LTL == expectedKind) {
        return isCorrectExp(car(exp), EXP_NEXT);
      }

      FALLTHROUGH

      /* unary operators compatible with LTL and CTL operator */
    case NOT:
    case UMINUS:
      return isCorrectExp(car(exp), expectedKind);

      /* binary opertors incompatible with LTL and CTL operator */
    case BIT_SELECTION:
    case CASE: case COLON:
    case CONCATENATION:
    case TIMES: case DIVIDE: case PLUS :case MINUS: case MOD:
    case LSHIFT: case RSHIFT: case LROTATE: case RROTATE:
    case WAREAD: case WAWRITE: /* AC ADDED THESE */
    case UNION: case SETIN:
    case EQUAL: case NOTEQUAL: case LT: case GT: case LE: case GE:
    case IFTHENELSE:
    case EXTEND:
    case WRESIZE:
    case CONST_ARRAY: /* AI ADDED */
      if (EXP_CTL == expectedKind) {
        return isCorrectExp(car(exp), EXP_SIMPLE)
          && isCorrectExp(cdr(exp), EXP_SIMPLE);
      }
      else if (EXP_LTL == expectedKind) {
        return isCorrectExp(car(exp), EXP_NEXT)
          && isCorrectExp(cdr(exp), EXP_NEXT);
      }

      FALLTHROUGH

      /* binary opertors compatible LTL and CTL operator */
    case AND: case OR: case XOR: case XNOR: case IFF: case IMPLIES:
      return isCorrectExp(car(exp), expectedKind)
        && isCorrectExp(cdr(exp), expectedKind);

      /* next expression (LTL is allowed to contain next) */
    case NEXT:
      if (EXP_NEXT != expectedKind &&
          EXP_LTL != expectedKind) {
        nusmv_yyerror_lined("unexpected 'next' operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_SIMPLE); /* NEXT cannot contain NEXT */

      /* CTL unary expressions */
    case EX: case AX: case EF: case AF: case EG: case AG:
    case ABU: case EBU:
    case EBF: case ABF: case EBG: case ABG:
      if (EXP_CTL != expectedKind) {
        nusmv_yyerror_lined("unexpected CTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_CTL); /* continue to check CTL */

      /* CTL binary expressions */
    case AU: case EU:
      if (EXP_CTL != expectedKind) {
        nusmv_yyerror_lined("unexpected CTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_CTL)
        && isCorrectExp(cdr(exp), EXP_CTL); /* continue to check CTL */


      /* LTL unary expressions */
    case OP_NEXT: case OP_PREC: case OP_NOTPRECNOT: case OP_GLOBAL:
    case OP_HISTORICAL: case OP_FUTURE: case OP_ONCE:
      if (EXP_LTL != expectedKind) {
        nusmv_yyerror_lined("unexpected LTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_LTL); /* continue to check LTL */


      /* LTL binary expressions */
    case UNTIL: case SINCE:
      if (EXP_LTL != expectedKind) {
        nusmv_yyerror_lined("unexpected LTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_LTL)
        && isCorrectExp(cdr(exp), EXP_LTL); /* continue to check LTL */

    default: nusmv_assert(false); /* unknown expression */
    }
  return false; /* should never be invoked */
}


static int nusmv_parse_psl()
{
  int res;
  res = psl_yyparse();
  return res;
}
  /* ENDS: grammar.y.3.50 */

