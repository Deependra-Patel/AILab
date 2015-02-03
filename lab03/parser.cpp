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

int exp::tokenize(char *arr, int l, int pos){
  while (arr[pos] == ' ') pos++;
  if ((arr[pos] >= 'a' && arr[pos] <= 'z') || arr[pos] == 'F'){
    mode = 1;
    id = arr[pos];
    return pos + 1;
  }
  else if (arr[pos] == '~'){
    mode = 2;
    op = 1;
    exp1 = new exp();
    pos = exp1->tokenize(arr, l, pos + 1);
    return pos;
  }
  else if (arr[pos] == '('){
    mode = 4;
    exp1 = new exp();
    pos = exp1->tokenize(arr, l, pos + 1);
    while (arr[pos] == ' ') pos++;
    if (arr[pos] == ')'){
	mode = 2;
	op = 0;
	return pos + 1;
    }
    if (arr[pos] == '^'){
      op = 2;
      pos += 1;
    }
    else if (arr[pos] == 'v'){
      op = 3;
      pos += 1;
    }
    else if (arr[pos] == '-' && arr[pos + 1] == '>'){
      op = 4;
      pos += 2;
    }
    exp2 = new exp();
    pos = exp2->tokenize(arr, l, pos);
    while(arr[pos] == ' ') pos++;
    return pos + 1;
  }
}

node::node(){
    leaf = 0;
    node1 = 0;
    node2 = 0;
    parent1 = 0;
    parent2 = 0;
}

node::node(char c1){
    leaf = 1;
    this->id = c1;
    this->node1 = 0;
    this->node2 = 0;
    this->parent1 = 0;
    this->parent2 = 0;
}

node* exp::Fnode(){
  node* n = new node();
  n->leaf = 1;
  n->id = 'F';
}

node* exp::makeTree(){
  if (mode & 1){
    node *n = new node();
    n->leaf = 1;
    n->id = id;
    return n;
  }
  else if (mode & 2){
      if(op == 1){
	  node *n;
	  n = new node();
	  n->leaf = 0;
	  n->node1 = exp1->makeTree();
	  n->node2 = Fnode();
	  return n;
      }
      else if(op == 0){
	  return exp1->makeTree();
      }
  }
  else if (mode & 4){
    node *n;
    n = new node();
    n->leaf = 0;
    if (op == 2){
      // and
      n->node1 = new node();
      n->node1->node1 = exp1->makeTree();
      n->node1->node2 = new node();
      n->node1->node2->node1 = exp2->makeTree();
      n->node1->node2->node2 = Fnode();
      n->node2 = Fnode();
      return n;
    }
    else if (op == 3){
      // or
      n->node1 = new node();
      n->node1->node1 = exp1->makeTree();
      n->node1->node2 = Fnode();
      n->node2 = exp2->makeTree();
      return n;
    }
    else if (op == 4){
      // imply
      n->node1 = exp1->makeTree();
      n->node2 = exp2->makeTree();
      return n;
    }
  }
}

void exp::printExp(){
  if (mode & 1){
    cout<<id;
  }
  else if (mode & 2){
      if (op == 1){
	  cout<<"(";
	  exp1->printExp();
	  cout<<"->F)";
      }
      else if(op == 0){
	  exp1->printExp();
      }
  }
  else if (mode & 4){
    cout<<"(";
    if (op == 2) {
      // and
      cout<<"(";
      exp1->printExp();
      cout<<"->";
      cout<<"(";
      exp2->printExp();
      cout<<"->F))->F";
    }
    else if (op == 3){
      // or
      cout<<"(";
      exp1->printExp();
      cout<<"->F)->";
      exp2->printExp();
    }
    else if (op == 4){
      // imply
      exp1->printExp();
      cout<<"->";
      exp2->printExp();
    }
    cout<<")";
  }
}
