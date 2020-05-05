#include "lists.h"

/**
* is_palindrome - Checks if a linked list is palindrome
* @head: Double pointer to linked list
* Return: 1 if palindrome, 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, j = 0, len;
	int arr[100], arr2[100];

	if (head == NULL)
		return (1);
	if (*head == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	len = i;
	i--;
	while (i >= 0)
	{
		arr2[j] = arr[i];
		j++, i--;
	}
	for (i = 0; i < len; i++)
	{
		if (arr[i] != arr2[i])
			return (0);
	}
	return (1);
}
