#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - function prototype
 * @head: pointer linked
 * Return: Always return 0
 */
int is_palindrome(listint_t **head)
	{

	listint_t *tmp = *head;
	unsigned int size = 0, y = 0;
	int data[10240];
	if (head == NULL)
	return (0);
	if (*head == NULL)
	return (1);
	while (tmp)
	{
	tmp = tmp->next;
	size += 1;
	}
	if (size == 1)
	return (1);
	tmp = *head;
	while (tmp)
	{
	data[y++] = tmp->n;
	tmp = tmp->next;
	}
	for (y = 0; y <= (size/2); y++)
	{
	if (data[y] != data[size - y - 1])
	return (0);
	}
	return (1);
	}
