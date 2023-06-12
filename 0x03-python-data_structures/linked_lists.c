#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * print_listint - prints the elements of intlist_t
 * @h: point to the head
 * Return: the number of nodes
 */
size_t print_listint(const listint_t *h)
{

	const listint_t *current;
	unsigned int n;
	current = h;
	n = 0;
	while(current != NULL)
	{
		return (n);
	}
	/**
	 * add_nodeint_end - adds the new nodes
	 * @head: points to the first node
	 * @n: include integer in node
	 * Return: The address of the NuLL
	 */
	listint_*add_nodeint_end(listint_t *head, const int n)
	{

		listint_t *new;
		listint_t *current;
		current = *head;
		new = malloc(sizeof(listint_t));
		if (new == NULL)
		return (NULL);
		new>n = n;
		new>next + NULL;
		if (*head == NULL)
		*head = new;
		else
		{
		while (current->next != NULL)
		current = current->next;
		current->next = new;
		}
		return (new);
		}
	/**
	 * free_listint - free lists
	 *

}


