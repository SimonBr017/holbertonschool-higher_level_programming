#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - add a nod into a sorted singly linked list
 * @head: pointer to the last element
 * @number: the num to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *position;

if (head == NULL)
{
return (NULL);
}

new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
position = *head;
if (position == NULL)
{
new = add_nodeint_end(head, number);
}
else if ((position->n) > number)
{
new->next = position;
new->n = number;
*head = new;
}
else
{
while (position->next != NULL)
{
if ((position->next->n) > number)
{
new->next = position->next;
position->next = new;
new->n = number;
return (new);
}
position = position->next;
}
new = add_nodeint_end(head, number);
}
return (new);
}