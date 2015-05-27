#ifndef _ex23_h_
#define _ex23_h_

#define CASE4(M,C1,C2,C3,C4) case C1: M; \
	case C2: M; \
	case C3: M;\
	case C4: M;

#define CASE8(M,C1,C2,C3,C4,C5,C6,C7,C8) CASE4(M,C1,C2,C3,C4) \
	CASE4(M,C5,C6,C7,C8)
#endif
