#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct
{
    char stack[20][20];
    int top;
    int capacity;
} BrowserHistory;

BrowserHistory *browserHistoryCreate(char *homepage);

BrowserHistory *browserHistoryCreate(char *homepage)
{
    BrowserHistory *result = (BrowserHistory *)malloc(sizeof(BrowserHistory));
    result->top = -1;
    result->capacity = 1;

    strncpy(result->stack[++result->top], homepage, strlen(homepage));
    result->stack[result->top][strlen(homepage)] = '\0';

    return result;
}

void browserHistoryVisit(BrowserHistory *obj, char *url);
void browserHistoryVisit(BrowserHistory *obj, char *url)
{
    while (obj->top != obj->capacity - 1)
    {
        free(obj->stack[obj->top]);
        obj->top--;
        obj->capacity--;
    }
    strncpy(obj->stack[++obj->top], url, strlen(url));
    obj->stack[obj->top][strlen(url)] = '\0';
    obj->capacity++;
}

char *browserHistoryBack(BrowserHistory *obj, int steps);
char *browserHistoryBack(BrowserHistory *obj, int steps)
{
    obj->top -= steps;
    if (obj->top < 0) {
        obj->top = 0;
    }
    return obj->stack[obj->top];
}

char *browserHistoryForward(BrowserHistory *obj, int steps)
{
    obj->top += steps;
    if (obj->top > obj->capacity) {
        obj->top = obj->capacity - 1;
    }
    return obj->stack[obj->top];
}

void browserHistoryFree(BrowserHistory *obj)
{
    free(obj->stack);
}

// Your BrowserHistory struct will be instantiated and called as such:
int main() {
    BrowserHistory* obj = browserHistoryCreate("homepage");
    printf("%s\n", obj->stack[0]);
    browserHistoryVisit(obj, "url");
    printf("%s\n", obj->stack[1]);
    browserHistoryVisit(obj, "urlsds");
    printf("%s\n", obj->stack[2]);
    char* param_2 = browserHistoryBack(obj, 1);
    printf("%s\n", param_2);
    char* param_3 = browserHistoryForward(obj, 1);
    printf("%s\n", param_3);
    browserHistoryFree(obj);

}
/**
 * browserHistoryVisit(obj, url);

 * char* param_2 = browserHistoryBack(obj, steps);

 * char* param_3 = browserHistoryForward(obj, steps);

 * browserHistoryFree(obj);
*/
