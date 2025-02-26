class CacheNode {
    key: number;
    val: number;
    prev: CacheNode | null;
    next: CacheNode | null;

    constructor(key: number, val: number) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    private capacity: number;
    private cache: Map<number, CacheNode>;
    private oldest: CacheNode;
    private latest: CacheNode;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map<number, CacheNode>();

        this.oldest = new CacheNode(0, 0);
        this.latest = new CacheNode(0, 0);
        this.oldest.next = this.latest;
        this.latest.prev = this.oldest;
    }

    private insert(node: CacheNode): void {
        node.prev = this.latest.prev;
        node.next = this.latest;
        this.latest.prev!.next = node;
        this.latest.prev = node;
    }

    private remove(node: CacheNode): void {
        const prev = node.prev;
        const next = node.next;
        next!.prev = prev;
        prev!.next = next;
    }

    get(key: number): number {
        if (this.cache.has(key)) {
            const node = this.cache.get(key)!;
            this.remove(node);
            this.insert(node);
            return node.val;
        }
        return -1;
    }

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            this.remove(this.cache.get(key)!);
        }

        const node = new CacheNode(key, value);
        this.cache.set(key, node);
        this.insert(node);

        if (this.cache.size > this.capacity) {
            const lru = this.oldest.next!;
            this.remove(lru);
            this.cache.delete(lru.key);
        }
    }
}