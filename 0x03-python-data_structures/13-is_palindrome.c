#include "lists.h"

/**
* is_palindrome - Checks if a linked list is palindrome
* @head: Double pointer to linked list
* Return: 1 if palindrome, 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, j = 0;
	int arr[100], arr2[100];

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	temp = *head;
	if (temp->next == NULL)
		return (1);
	while (temp != NULL)
	{
		arr[i] = temp->n;
		arr2[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i--;
	while (i >= 0)
	{
		if (arr[i] != arr2[j])
			return (0);
		i--, j++;
	}
	return (1);
}
