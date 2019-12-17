#include "lists.h"
/**
* is_palindrome- checks if a list is palindrom
* @head: double pointer to the first element
*
* Description: this function prints all elements of a list
* Return: 1 if the list is palindrome 0 if not
*/
int is_palindrome(listint_t **head)
{
	size_t nodes = 0;
	unsigned int i = 1, j, x;
	listint_t *tmp = *head, *backwards;

	if (*head == NULL || head == NULL)
		return (1);
	while (tmp)
	{
		tmp = tmp->next;
		nodes++;
	}
	x = nodes / 2;
	tmp = *head;
	while (i <= x)
	{
		backwards = tmp, j = i;
		while (j <= (nodes - i))
			backwards = backwards->next, j++;
		if (tmp->n != backwards->n)
			return (0);
		tmp = tmp->next, i++;
	}
	return (1);
}
