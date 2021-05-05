#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to listin_t head of list
 * Return: 1 if true or 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i = 0;
	int j = 0;
	int array[2048];
	int limit;

	if (*head == NULL || head == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		array[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	limit = (i % 2 == 0) ? i / 2 : (i + 1) / 2;
	for (j = 0; j < limit; j++)
	{
		if (array[j] != array[i - 1 - j])
			return (0);
	}
	return (1);
}
