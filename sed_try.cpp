// ...existing code...
#include "rb_tree.h"

int main()
{
    RBTree<int> tree;
    tree.insert(10);
    tree.insert(20);
    tree.insert(30);
    tree.insert(15);

    std::cout << "中序遍历: ";
    tree.inorder();

    std::cout << "查找25: " << (tree.search(25) ? "找到" : "未找到") << std::endl;
    return 0;
}
// ...existing code...