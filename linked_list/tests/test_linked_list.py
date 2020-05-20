from linked_list.linked_list import LinkedList

def test_one():
    actual = LinkedList.insert(3)
    expected = 3
    assert actual == expected