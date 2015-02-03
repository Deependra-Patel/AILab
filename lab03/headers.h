#include <vector>
using namespace std;

struct node{
  int leaf;
  node *node1, *node2;
  node* parent1;
  node* parent2;
  char id;
  node();
  node(char);
  int isEqual(node*);
  node* contraPositive();
  node* axiom1();
  node* axiom2();
  node* axiom3();
};


struct exp{
  int mode;
  exp *exp1, *exp2;
  int op;
  char id;
  int tokenize(char*, int, int);
  void printExp();
  node* Fnode();
  node* makeTree();
};

void reduce(node*);
void printNode(node*);
void printReducedForm(vector<node*>);
bool bfs();
