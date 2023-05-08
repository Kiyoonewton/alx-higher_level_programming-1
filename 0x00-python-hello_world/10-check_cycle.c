#include "lists.h"

/**
 * check_cycle - to checks if a linked list contains a cycle
 * @list: my linked list to check
 *
 * Return: always 1 if the list has a cycle and 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
