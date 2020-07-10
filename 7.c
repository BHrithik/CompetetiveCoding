int stack[10000000],min_stack[10000000];
int tp=-1,min_top=-1;

void init() {
    tp=-1;
    min_top=-1;
}

void push(int x) {
    stack[++tp]=x;
    if (min_top==-1 || x<min_stack[min_top])
        min_stack[++min_top]=x;
}

void pop() {
    if (tp==-1)
        return;
    if (stack[tp]==min_stack[min_top])
        min_top--;
    tp--;
}

int top() {
    if (tp==-1)
        return -1;
    return stack[tp];
}

int getMin() {
    if (min_top==-1)
        return -1;
    return min_stack[min_top];
}