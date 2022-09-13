public class LinkedList{
	private Node head;

	LinkedList(){}

	public void add(Object data){
		Node current = head;
		if(head==null){
			head = new Node(data);
			return;
		}
		
		while(current.next != null){
			current = current.next;
		}
		current.next = new Node(data);
	}

	public boolean remove(Object data){
		Node current = head;
		Node prev = null;
		if(current==null){
			return false;
		}
		while(current.next!=null && current.data != data){
			prev = current;
			current = current.next;
		}

		if(current.data == data){ //found it
			if(prev!=null){
				prev.next = current.next;
			}
			else{
				head = current.next;
			}
			return true;
		}
		else{
			return false;
		}
	}

	public int length(){
		Node current = head;
		int i = 0;
		while(current!=null){
			i++;
			current = current.next;
		}
		return i;
	}

	public Object getAtIndex(int index){
		int len = length();
		Node current = head;

		if(index>=len){
			return null;
		}
		
		for(int i=0; i<len; i++){
			current = current.next;
		}
		return current.data;
	}
}