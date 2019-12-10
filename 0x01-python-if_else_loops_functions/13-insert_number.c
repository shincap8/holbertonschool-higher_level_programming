#include "lists.h"
#include <stddef.h>
#include <stdarg.h>
#include <stdio.h>
/**
* insert_node- inserts a new node in x position
* @head: pointer to the first element
* @number: int of the new node
*
* Description: this function add a node in a specific order
* Return: the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *aux = *head, *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	while (aux)
	{
		tmp = aux->next;
		if (number < aux->n)
		{
			*head = new;
			new->next = aux;
			return (new);
		}
		if (aux->next == NULL)
		{
			aux->next = new;
			return (new);
		}
		if (number >= aux->n && number < tmp->n )
		{
			new->next = aux->next;
			aux->next = new;
			return (new);
		}
		aux = aux->next;
	}
	return (NULL);
}
