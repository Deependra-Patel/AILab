#include <iostream>
#include <string>
#include <stack>
using namespace std;

//inp will be of the form (Exp)
string convert(string inp){
    stack<char> st;
    for(int i = 0; i < inp.length(); i++){
	char op;
	string left, right;
	if(inp[i] == '(') st.push('(');
	else if(inp[i] == ')') st.pop();
	if(st.empty()){
	    string c_left = convert(left);
	    op = inp
	}
	left += inp[i];	

    st.push_back(inp[0]);
}

int main(){
}
