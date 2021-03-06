#include "lists.h"
/**
  * check_cycle - Function that check if a
  * singly linked list has a cycle in it
  * @list: pointer to a list
  * Return: 0 if there is no cycle, 1 if there
  * is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow_p = NULL, *fast_p = NULL;

	if (list == NULL || list->next == NULL)
		return (0);

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
