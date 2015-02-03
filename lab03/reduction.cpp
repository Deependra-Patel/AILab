#include <iostream>
#include <string>
#include <vector>
#include "headers.h"
using namespace std;

vector<node* > literals;
void reduce(node* tree){
    //cout<<"leafVal: "<<tree->leaf<<endl;
    //printNode(tree);
    // if the node is a leaf
    if(tree->leaf == 1 && tree->id != 'F'){
	node* ins = new node();
	//node2 is the node denoting f
	node* nodeF = new node();
	nodeF->leaf = 1;
	nodeF->id = 'F';
	ins->node1 = tree;
	ins->node2 = nodeF;
	literals.push_back(ins);
	//cout<<"yo"<<endl;
    }
    else if(tree->leaf == 0){
	//cout<<"imhere\n";
	node* ins = tree->node1;
	literals.push_back(ins);
	//cout<<ins->id<<endl;
	reduce(tree->node2);
    }
}

void printReducedForm(vector<node* > V){
    for(int i = 0; i < V.size(); i++){
	node* toBePrinted = V[i];
	printNode(toBePrinted);
	if(i != V.size()-1) cout<<", ";
    }
    cout<<" |- "<<"F"<<endl;
}

void printNode(node* toBePrinted){
    if(!toBePrinted) return;
    if(toBePrinted->leaf == 1){
	cout<<toBePrinted->id;
    }
    else{
	cout<<"(";
	printNode(toBePrinted->node1);
	cout<<"->";
	printNode(toBePrinted->node2);
	cout<<")";
    }
   
 
}
