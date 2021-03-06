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
	tmp2 = tmp2->next;
	while (tmp1 != NULL && tmp2 != NULL && tmp2->next != NULL)
	{
		if (tmp1 == tmp2)
		{
			return (1);
		}
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
	}
	return (0);
}
