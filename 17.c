bool has_only_spaces(const std::string& str) {
return str.find_first_not_of(’ ') == str.npos;
}

vector Solution::prettyJSON(string str){
vector sol;
int n=str.length();
int i=0;
string line="";
int spaces=0;
while(i<n){
string idn="";
for(int j=0;j<spaces;++j) idn += “\t”;
if(str[i] == ‘{’ || str[i] == ‘[’){
if(!line.empty() && !has_only_spaces(line)){
sol.push_back(idn+line);
}
line.clear();
sol.push_back(idn+str[i]);
++spaces;
}
else if(str[i] == ‘,’){
if(i-1>=0 && (str[i-1] == ‘]’ || str[i-1]==’}’)){
int k = sol.size()-1;
sol[k] += “,”;
}
else{
line += “,”;
sol.push_back(idn+line);
line.clear();
}
}
else if(str[i] == ‘}’ || str[i] == ‘]’){
if(!line.empty() && !has_only_spaces(line)){
sol.push_back(idn+line);
}
line.clear();
–spaces;
idn = “”;
for(int j=0;j<spaces;++j) idn += “\t”;
sol.push_back(idn+str[i]);
}
else{
line += str[i];
}
++i;
}
return sol;
}