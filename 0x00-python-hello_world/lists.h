
#ifndef Lists_H
#define Lists_H

#include <stdlib.h>

/**
 * struct listint_s - This is singly lists structure
 * @n: integer
 * @next: This will point to the next node
 *
 * Description: singly linked list
 */

typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);

#endif
