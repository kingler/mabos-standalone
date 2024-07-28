/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

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




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 138 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
{
  node_ptr node;
  int lineno;
}
/* Line 1529 of yacc.c.  */
#line 342 "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE nusmv_yylval;

