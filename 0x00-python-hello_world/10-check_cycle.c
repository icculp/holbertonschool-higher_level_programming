#include "lists.h"

/**
* check_cycle - Checks if a linked list has a cycle in it
* @list: Pointer to linked list
* Return: Success or fail
*/

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
