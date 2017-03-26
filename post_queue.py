import os
import json

class Queue():
    def __init__(self, head):
        self.head = head
        self.length = 0


    def enqueue(self, new_entry):
        self.head.prev = new_entry
        new_entry.next = self.head
        self.head = new_entry
        self.length += 1

    def dequeue(self):
        old_head = self.head
        self.head = old_head.next
        old_head.next = None
        self.head.prev = None
        self.length -= 1

    def print_q(self):
        print('—————')
        print('queue len : ', self.length+1)
        this_entry = self.head
        i=0
        while i<=self.length:
            print(this_entry.pid)
            this_entry = this_entry.next
            i+=1
        print('—————')

class Entry():
    def __init__(self, source, pid, description, img):
        self.source = source
        self.pid = pid
        self.description = description
        self.img = img
        self.next = None
        self.prev = None

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

# e = Entry('a','b','c','d')
# q = Queue(e)
#
# q.enqueue(e)
# e = Entry('a','c','c','d')
# q.enqueue(e)
#
# q.print_q()
# q.dequeue()
#
# q.print_q()

# print(os.path.getsize('post_map'))
data = {}
data['key'] = 'value'
json_data = json.dumps(data)
data['key2'] = 'value2'
json_data = json.dumps(data)
data['key'] = 'value'
json_data = json.dumps(data)
# print(json_data)

data2 = {}
data2['key'] = 'value'
json_data2 = json.dumps(data2)
with open("post_map", "w") as f:
    json.dump(json_data, f)
    # json.dump(json_data2, f)

with open("post_map", "a") as f:
    json.dump(json_data2, f)

# with open("post_map", "r") as f:
#     file_data = json.loads(f)
    # print(file_data)