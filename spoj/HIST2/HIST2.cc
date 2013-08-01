#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <cassert>
#include <queue>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <math.h>

#define GI ({int y;scanf("%d",&y);y;})
#define REP(i,N) for(int i = 0;i<(N);i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i )
#define LET(x,a) __typeof(a) x(a)
#define sz size()
#define cs c_str()
#define REPV(i,ar) for(int i = 0;i<int((ar).size());i++)
#define EACH(it,mp) for(__typeof(mp.begin()) it(mp.begin());it!=mp.end();it++)
#define pb push_back
#define sor(ar) sort(ar.begin(),ar.end())
#define LINF (1e18)
#define INF (1<<30)
#define rev(ar) reverse(ar.begin(),ar.end())


using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VPI;



int main() {
	int N;
	int e[15];
	int bitall;
	int score[15],paths[15],bitmask[15];
	int _score[15],_paths[15],_bitmask[15];
	int maxscore = 0,maxid=-1;	

	REP(i,15) score[i]=_score[i]=paths[i]=_paths[i]=bitmask[i]=_bitmask[i]=0;

	while(N = GI){
//		cout<<N<<endl;
		REP(i,N) e[i] = GI;
		bitall = (1<<N)-1;
//		REP(i,N) cout<<e[i]<<" ";  cout<<endl;
		REP(i,N) {
			if (i==0) REP(j,N) {
				_score[j]=e[j];
				_paths[j] = 1;
				_bitmask[j] = bitall^(1<<j);
			} else if(i< N-1){ 
				REP(j,N) { 
					REP(k,N) { 
						if(!(_bitmask[k]&(1<<j))) continue;
						else if( abs(e[j]-e[k])+_score[k]>=score[j]) {
							score[j] = abs(e[j]-e[k]) + _score[k];
							bitmask[j] = _bitmask[k]^(1<<j);
						}
					}
					REP(k,N) { 
						if(!(_bitmask[k]&(1<<j))) continue;
						else if( abs(e[j]-e[k])+_score[k] == score[j]) {
							paths[j] += _paths[k];
						}
					}
				}
				REP (j,N) {_score[j] = score[j],_paths[j] = paths[j],_bitmask[j] = bitmask[j];
					score[j] = paths[j] = bitmask[j] = 0;	
				}				
			} else { 
				REP(j,N) { 
					REP(k,N) { 
						if(!(_bitmask[k]&(1<<j))) continue;
						else if( e[j]+abs(e[j]-e[k])+_score[k]>=score[j]) {
							score[j] = abs(e[j]-e[k])+e[j] + _score[k];
							bitmask[j] = _bitmask[k]^(1<<j);
						}
					}
					REP(k,N) { 
						if(!(_bitmask[k]&(1<<j))) continue;
						else if(e[j]+abs(e[j]-e[k])+_score[k] == score[j]) paths[j] += _paths[k]+1;
					}
				}						
			}
		}
		maxscore = 0;
		REP(i,N) {
			if (score[i] > maxscore) maxscore=score[i],maxid=i;

		}
		cout<<maxscore+2*N<<" "<<paths[maxid]<<endl;
	}

	return 0;
}
