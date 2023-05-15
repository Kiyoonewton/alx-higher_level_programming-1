#include "lists.h"

/**
 * is_palindrome - function to call to_check_mypal to see if list is palindrome
 * @head: pointer to the beginning of the list
 * Return: 1 if palindrom else 0
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (to_check_mypal(head, *head));
}

/**
 * to_check_mypal - function to check if the list is palindrome
 * @head: pointer to the beggining of the list
 * @last: pointer to the end of the list
 *
 * Return: 1 if palindrom else 0
 */

int to_check_mypal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);

	if (to_check_mypal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
