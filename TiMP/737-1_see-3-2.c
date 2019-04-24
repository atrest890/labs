#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int value;
    struct node *next;
    struct node *prev;
} node;

typedef struct list {
    node *head;
    node *tail;
} list;

void init(list *l) {
    l->head = NULL;
    l->tail = NULL;
}

void clear(list *l) {
    node *n = l->head;

    while (n != NULL) {
        node *p = n->next;
        free(n);
        n = p;
    }
}

int isEmpty(list *l) {
    if (l->head == NULL) {
        return 1;
    }

    return 0;
}

node* find(list *l, int value) {
    node *n = l->head;

    while (n != NULL && n->value != value) {
        n = n->next;
    }

    return n;
}

int push_back(list *l, int value) {
    node *n = malloc(sizeof(node));
    n->value = value;
    n->next = NULL;
    n->prev = NULL;
    node *p = l->tail;

    if ( isEmpty(l) ) {
        l->head = n;
        l->tail = n;
    }
    else {
        p->next = n;
        n->prev = p;
        l->tail = n;
    }

    return 0;
}

int push_front(list *l, int value) {
    node *n = malloc(sizeof(node));
    n->value = value;
    n->next = NULL;
    n->prev = NULL;

    if ( isEmpty(l) ) {
        l->head = n;
        l->tail = n;
    }
    else {
        node *p = l->head;
        p->prev = n;
        n->next = p;
        l->head = n;
    }

    return 0;
}

int insertAfter(node *n, int value) {
    node *p = malloc(sizeof(node));
    p->value = value;
    n->next->prev = p;
    p->next = n->next;
    p->prev = n;
    n->next = p;
    return 0;
}

int insertBefore(node *n, int value) {
    node *p = malloc(sizeof(node));
    p->value = value;
    n->prev->next = p;
    p->next = n;
    p->prev = n->prev;
    n->prev = p;
    return 0;
}

int removeFirst(list *l, int value) {
    node *n = l->head;

    while (n != NULL && n->value != value) {
        n = n->next;
    }

    if (n == NULL) {
        return -1;
    }

    if (n == l->head) {
        l->head = n->next;

    }
    if (n == l->tail) {
        l->tail = n->prev;
    }
    if (n->prev != NULL) {
        node *p = n->prev;
        p->next = n->next;
    }
    if (n->next != NULL) {
        node *p = n->next;
        p->prev = n->prev;
    }

    free(n);

    return 0;
}

void print(list *l) {
    node *temp = l->head;

    while (temp != NULL) {
        printf("%d ", temp->value);
        temp = temp->next;
    }
    printf("%c", '\n');
}

void print_inverse(list *l) {
    node *temp = l->tail;

    while (temp != NULL) {
        printf("%d ", temp->value);
        temp = temp->prev;
    }
    printf("%c", '\n');
}

int removeLast(list *l, int value) {
    node *n = l->tail;

    while (n != NULL && n->value != value) {
        n = n->prev;
    }

    if (n == NULL) {
        return -1;
    }

    if (n == l->head) {
        l->head = n->next;

    }
    if (n == l->tail) {
        l->tail = n->prev;
    }
    if (n->prev != NULL) {
        node *p = n->prev;
        p->next = n->next;
    }
    if (n->next != NULL) {
        node *p = n->next;
        p->prev = n->prev;
    }

    free(n);

    return 0;

}

int main()
{
    list *lst = malloc(sizeof(list));

    //task 1
    int n;
    scanf("%d", &n);

    //task 2
    init(lst);
    int a;
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a);
        push_back(lst, a);
    }

    //task 3
    print(lst);

    //task 4
    int nodes[3] = {};
    scanf("%d %d %d", &nodes[0], &nodes[1], &nodes[2]);

    for (int i = 0; i < 3; ++i) {
        node *n = find(lst, nodes[i]);

        if (n != NULL) {
            printf("%d", 1);
        }
        else {
            printf("%d", 0);
        }
    }
    printf("%c", '\n');


    //task 5
    int m;
    scanf("%d", &m);
    push_back(lst, m);

    //task 6
    print_inverse(lst);

    //task 7
    int t;
    scanf("%d", &t);
    push_front(lst, t);

    //task 8
    print(lst);

    //task 9
    int j, x;
    scanf("%d %d", &j, &x);

    node *p = lst->head;

    for (int i = 1; i < j; ++i) {
        p = p->next;
    }

    insertAfter(p, x);

    //task 10
    print_inverse(lst);

    //task 11
    int u, y;
    scanf("%d %d", &u, &y);

    node *l = lst->head;

    for (int i = 1; i < u; ++i) {
        l = l->next;
    }

    insertBefore(l, y);

    //task 12
    print(lst);

    //task 13
    int z;
    scanf("%d", &z);
    removeFirst(lst, z);

    //task 14
    print_inverse(lst);

    //task 15
    int r;
    scanf("%d", &r);
    removeLast(lst, r);

    //task 16
    print(lst);

    //task 17
    clear(lst);

    return 0;
}
