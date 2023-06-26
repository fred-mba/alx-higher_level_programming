#include "lists.h"

/**
 * check_cycle - cycle check in a list
 * @list: pointer to beginning of the node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *find;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	find = current->next;

	while (current != NULL && find->next != NULL
		&& find->next->next != NULL)
	{
		if (current == find)
			return (1);
		current = current->next;
		find = find->next->next;
	}
	return (0);
}
