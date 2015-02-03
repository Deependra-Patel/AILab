#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
#include <stack>
#include <vector>
#include <queue>
#include "headers.h"
using namespace std;


#define fore(i, l, r) for(int i = l; i < r; i++)
#define forn(i, n) fore(i, 0 ,n)

extern vector<node* > literals;

int node::isEqual(node* n){
    if (leaf != n->leaf) return 0;
    else if (leaf == 1){
	return id == n->id;
    }
    else{
	return node1->isEqual(n->node1) && node2->isEqual(n->node2);
    }
}

int satisfyMP(node* n1, node* n2){
    if (n2->leaf) return 0;
    else return n1->isEqual(n2->node1);
}

bool isPresent(node* cur){
    int l = literals.size();
    for(int i = 0; i<l; i++){
	if (cur->isEqual(literals[i])) return true;
    }
    return false;
}

node* node::contraPositive(){
    //cout<<"Contra: "<<endl;
    //printNode(this);
    //cout<<endl;
    if (this->leaf) return 0;
    node * f1 = new node('F');
    node * f2 = new node('F');
    node * top = new node();
    node * left = new node();
    node * right = new node();
    
    if (!node2->leaf && node2->node2->id ==  'F'){
	left = node2->node1;
    }
    else{
	left->node1 = this->node2;
	left->node2 = f1;
    }
    if (!node1->leaf && node1->node2->id ==  'F'){
	right = node1->node1;
    }
    else{
	right->node1 = this->node1;
	right->node2 = f2;
    }
    top->node1 = left;
    top->node2 = right;
    return top;
}

node* node::axiom2(){
    if (!node1 || !node2 || !node2->node1 || !node2->node2){
	return NULL;
    }
    node* top = new node();
    node* left = new node();
    node* right = new node();
    left->node1 = node1;
    left->node2 = node2->node1;
    right->node1 = node1;
    right->node2 = node2->node2;
    top->node1 = left;
    top->node2 = right;
    return top;
}

node* node::axiom3(){
    if (!node1 || !node2 || !node1->node1 || !node1->node2){ 
	return 0;
    }
    if ((node1->node2->leaf && node1->node2->id == 'F') && (node2->leaf && node2->id == 'F')){
	node* ret = new node();
	ret->node1 = node1->node1->node1;
	ret->node2 = node1->node1->node2;
	return ret;
    }
    else return 0;
}

node* node::axiom1(){
    if (!leaf && node2->id == 'F' && !node1->leaf){
	//cout<<"Axiom1: "<<endl;
	//printNode(this);
	//cout<<endl;
	node* final = new node();
	node* left;
	left = node1->node2;
	node* right;
	right = node1;
	final->node1 = left;
	final->node2 = right;
	//cout<<"After Axiom1: "<<endl;
	//printNode(final);
	//cout<<endl;
	return final;
    }
    return 0;
}


node* copy(node* n){
    node* ret = new node();
    ret->leaf = n->leaf;
    ret->node1 = n->node1;
    ret->node2 = n->node2;
    ret->id = n->id;
}

vector<node*> allChildren(node* cur){
    vector<node*> children;
    int l = literals.size();
    for(int i=0; i<l; i++){
	if(satisfyMP(cur, literals[i])){
	    node* child = copy(literals[i]->node2);
	    //child->node1 = literals[i]->node2->node1;
	    //child->node2 = literals[i]->node2->node2;
	    children.push_back(child);
	    child->parent1 = cur;
	    child->parent2 = literals[i];
	    
	}
	else if(satisfyMP(literals[i], cur)){
	    node* child = copy(cur->node2);
	    //child->node1 = cur->node2->node1;
	    //child->node2 = cur->node2->node2;
	    children.push_back(child);
	    child->parent1 = cur;
	    child->parent2 = literals[i];
	    //children.push_back(cur->node2);
	    //literals[i]->node2->parent1 = cur;
	}
    }
    
    node* child = new node();
    child = cur->contraPositive();
    if (child){
	child->parent1 = cur;
	children.push_back(child);
    }
    else 
	delete(child);
    
     
    node* child1;
    child1 = cur->axiom1();
    if (child1){
	child1->parent1 = cur;
	children.push_back(child1);
    }
    else 
	delete(child1);

    
    node* child2 = new node();
    child2 = cur->axiom2();
    if (child2){
	child2->parent1 = cur;
	children.push_back(child2);
    }
    else 
	delete(child2);

    node* child3 = new node();
    child3 = cur->axiom3();
    if (child3){
	child3->parent1 = cur;
	children.push_back(child3);
    }
    else 
	delete(child3);
    
    return children;
}

bool isVisited(node* cur){
    if(isPresent(cur))
	return true;
    else {
	literals.push_back(cur);
	return false;
    }
}
bool isFinal(node* cur){
    return cur->leaf && cur->id == 'F';
}

void printPath(node* n){
    if (n != NULL){
	printPath(n->parent1);
	printPath(n->parent2);
	printNode(n);
	if(n->parent1 && n->parent2){
	    cout<<" Derived From: {";
	    printNode(n->parent1);
	    cout<<",";
	    printNode(n->parent2);
	    cout<<"}";
	}
	cout<<endl;
    }
}

bool bfs(){
    queue<node*> myqueue;
    int l = literals.size();
    for (int i = 0; i < l; ++i){
	myqueue.push(literals[i]);
    }

    int threshold = 20;
    while(!myqueue.empty() && threshold){
	//cout<<threshold<<endl;
	node* curNode = myqueue.front();
	myqueue.pop();
	vector<node*> children = allChildren(curNode);
	for(int i = 0; i<children.size(); i++){
	    node* child = children[i];
	    if(!isVisited(child)){
		if(isFinal(child)){
		    cout<<"Node Found"<<endl<<endl;
		    printPath(child);
		    return true;
		    break;
		}
		else myqueue.push(child);
	    }
	}
	threshold --;
    }
    return false;
}
