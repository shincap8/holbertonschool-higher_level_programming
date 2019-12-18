#include "lists.h"
/**
* is_palindrome- checks if a list is palindrome
* @head: double pointer to the first element
*
* Description: this function prints all elements of a list
* Return: 1 if the list is palindrome 0 if not
*/
int is_palindrome(listint_t **head)
{
        size_t nodes = 0;
        unsigned int i = 1, j, x;
        int tmp[1000] ;

        if (*head == NULL || head == NULL)
                return (1);
        while (*head)
        {
                tmp[nodes] = (*head)->n;
                *head = (*head)->next;
                nodes++;
        }
        x = nodes / 2;
        for (i = 0; i <= x; i++)
        {
                j = nodes - i - 1;
                if (tmp[i] != tmp[j])
                        return (0);
        }
        return (1);
}
