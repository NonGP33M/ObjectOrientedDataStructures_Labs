else:
            allMoved = False
            while(not allMoved):
                allMoved = True
                present = self.head
                for i in range(self.getSize()):
                    if present != self.tail:
                        present = present.next
                    temp = present.prev.data
                    if int(temp) > int(present.data):
                        self.remove(temp)
                        self.append(temp)
                        allMoved = False

        present = self.head
        for i in range(self.getSize()):
            if present.data % self.div != present.data:
                present.done = 1
            present = present.next