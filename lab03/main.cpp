#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
#include <stack>
#include <vector>
#include "headers.h"
using namespace std;


#define fore(i, l, r) for(int i = l; i < r; i++)
#define forn(i, n) fore(i, 0 ,n)

extern vector<node* > literals;



int main(){
  int i;
  cin>>i;
  int temp = i;
  while(i--){
      literals.clear();
      cout<<endl<<endl<<"Case"<<temp-i<<": "<<endl;
      char arr[100];
      scanf(" %[^\n]s", arr);
      int l = strlen(arr);
      forn(i, l){
	  arr[l - i] = arr[l - i - 1];
      }
      arr[0] = '(';
      arr[l + 1] = ')';
      l += 2;

      exp *exp1 = new exp();
      exp1->tokenize(arr, l, 0);
      cout<<"Parsed Exp is "<<endl;
      exp1->printExp();
      cout<<endl;
      node* root = exp1->makeTree();
      printNode(root);
      cout<<endl;
      reduce(root);
      cout<<endl<<"After Reduction: "<<endl;
      printReducedForm(literals);
      cout<<endl;
  
      for(int i = 0; i<literals.size(); i++){
	  cout<<i<<" ";
	  printNode(literals[i]);
	  cout<<endl;
      }
      cout<<endl;
      bool found = bfs();
      if (!found) cout<<"Node not found"<<endl;
  }
 
}


