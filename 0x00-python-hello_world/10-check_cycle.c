#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *@list: linked list
 *Return: 1 if the list has a cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp1 = list;
	listint_t *tmp2 = list;

	if (list == NULL)
		return (0);

	while (tmp1 && tmp2 && tmp2->next)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
		if (tmp1 == tmp2)
			return (1);
	}
	return (0);
}
