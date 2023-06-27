#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in sorted order
 * @head: pointer-pointer to the head of the list
 * @number: number to add in the list
 * Return: the updated list with the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (head == NULL)
		return (NULL);

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Assign values to the new node */
	new_node->n = number;
	new_node->next = NULL;

	/* If the list is empty or the new node is smaller than the head */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}

	current = *head;

	/* Find the appropriate position to insert the new node */
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* Insert the new node */
	new_node->next = current->next;
	current->next = new_node;

	return (*head);
}
