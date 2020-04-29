#include "lists.h"

/**
* insert_node - Inserts a node into a sorted linked list
* @head: Double pointer to head
* @number: Number value to store in new node
* Return: Address of new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	temp = *head;
	new->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (temp->next == NULL)
	{
		if (number < temp->n)
		{
			new->next = temp;
			*head = new;
		}
		else
		{
			temp->next = new;
			new->next = NULL;
		}
		return (new);
	}
	while (temp->next != NULL)
	{
		if (number <= temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	new->next = NULL;
	return (new);
}
