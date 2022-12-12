#include "lists.h"

/**
 * insert_node - insert a number into a singly-linked list
 * @head: pointer to the head of the linked list
 * @number: the number to insert
 * Author: Adewale Liadi
 * Return: Null if pointer fails
 * 	otherwise - pointer to a new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return(NULL);
	new->n = number;

	if(node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}
