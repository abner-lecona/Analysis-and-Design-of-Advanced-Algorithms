# ----------------------------------------------------------
# Lab #2: Ordered Set Class
#
# Date: 20-Sep-2023
# Authors:
#           A01748222 Joahan Javier Garcia Fernandez
#           A01753179 Abner Maximiliano Lecona Nieves
# ----------------------------------------------------------

from __future__ import annotations
import types
from typing import Any, Generic, TypeVar, cast
from collections.abc import Iterable, Iterator

T = TypeVar('T')
N = TypeVar('N')
I = TypeVar('I')


class OrderedSet(Generic[T]):

    class __Node(Generic[N]):

        info: N | None
        next: OrderedSet.__Node[N]
        prev: OrderedSet.__Node[N]

        def __init__(self, value: N | None = None) -> None:
            self.info = value
            self.next = self
            self.prev = self

    class __Iterator(Generic[I]):

        __sentinel: OrderedSet.__Node[I]
        __current: OrderedSet.__Node[I]

        # Complexity: O(1)
        def __init__(self, sentinel: OrderedSet.__Node[I]) -> None:
            self.__sentinel = sentinel
            self.__current = self.__sentinel.next

        # Complexity: O(1)
        def __iter__(self) -> Iterator[I]:
            return self

        # Complexity: O(1)
        def __next__(self) -> I:
            if self.__current == self.__sentinel:
                raise StopIteration
            result = cast(I, self.__current.info)
            self.__current = self.__current.next
            return result

    __sentinel: OrderedSet.__Node[T]
    __count: int

    # Complexity: O(N^2)
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = OrderedSet.__Node()
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node = OrderedSet.__Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def __repr__(self) -> str:
        if self:
            return f'OrderedSet({list(self)})'
        return 'OrderedSet()'

    # Complexity: O(N)
    def __contains__(self, value: T) -> bool:
        # current = self.__sentinel.next
        # while current != self.__sentinel:
        #     if current.info == value:
        #         return True
        #     current = current.next
        # return False
        for elem in self:
            if elem == value:
                return True
        return False

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(1)
    def __iter__(self) -> Iterator[T]:
        return OrderedSet.__Iterator(self.__sentinel)

    # Compleity: O(N)
    def discard(self, value: T) -> None:
        current = self.__sentinel.next
        while current != self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__count -= 1
                return
            current = current.next

    # Complexity: O(N^2)
    def __eq__(self, other: object) -> bool:
        if isinstance(other, OrderedSet) and len(self) == len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True
        else:
            return False

    def __le__(self, other: OrderedSet[T]) -> bool:
        if len(self) <= len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True
        else:
            return False

    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result_and: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result_and.add(elem)
        return result_and

    def __sub__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result_sub: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem not in other:
                result_sub.add(elem)
        return result_sub

    def remove(self, value: T) -> None:
        if value not in self:
            raise KeyError()
        current = self.__sentinel.next
        while current != self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__count -= 1
                return
            current = current.next

    def __lt__(self, other: OrderedSet[T]) -> bool:
        for elem in self:
            if elem not in other:
                return False
        if self == other:
            return False
        return True

    def __ge__(self, other: OrderedSet[T]) -> bool:
        for elem in other:
            if elem not in self:
                return False
        return True

    def __gt__(self, other: OrderedSet[T]) -> bool:
        for elem in other:
            if elem not in self:
                return False
        if self == other:
            return False
        return True

    def isdisjoint(self, other: OrderedSet[T]) -> bool:
        for elem in self:
            if elem in other:
                return False
        return True

    def __or__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result_or: OrderedSet[T] = OrderedSet()
        for elem in self:
            result_or.add(elem)
        for elem in other:
            if elem not in result_or:
                result_or.add(elem)
        return result_or

    def __xor__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result_xor: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem not in other:
                result_xor.add(elem)
        for elem in other:
            if elem not in self:
                result_xor.add(elem)
        return result_xor

    def clear(self) -> None:
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel
        self.__count = 0

    def pop(self) -> T:
        if not self:
            raise KeyError()
        last_element = self.__sentinel.prev.info
        self.__sentinel.prev = self.__sentinel.prev.prev
        self.__sentinel.prev.next = self.__sentinel
        self.__count -= 1
        return last_element  # type: ignore


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet([4, 8, 15, 16, 23, 42])
