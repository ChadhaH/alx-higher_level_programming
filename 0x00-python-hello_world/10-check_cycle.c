#include "lists.h"

/**
 * check_cycle - function
 * @list: variable
 * Return: 0 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listing_t *fast = list;

	if (list == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
