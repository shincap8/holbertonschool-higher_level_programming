#include "lists.h"
#include <stddef.h>
#include <stdarg.h>
#include <stdio.h>
/**
* check_cycle- finds the loop in the linked list
* @head: pointer to the first element
*
* Description: this function finds a loop in the linked list
* Return: the address of the node where the loop starts
*/
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	while (list)
	{
		if ((list->next) >= list)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
