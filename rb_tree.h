#pragma once
#include <iostream>

enum Color { RED, BLACK };

template<typename T>
struct RBNode {
    T data;
    Color color;
    RBNode *left, *right, *parent;
    RBNode(T val) : data(val), color(RED), left(nullptr), right(nullptr), parent(nullptr) {}
};

template<typename T>
class RBTree {
private:
    RBNode<T>* root;

    void leftRotate(RBNode<T>*& root, RBNode<T>* x) {
        RBNode<T>* y = x->right;
        x->right = y->left;
        if (y->left) y->left->parent = x;
        y->parent = x->parent;
        if (!x->parent)
            root = y;
        else if (x == x->parent->left)
            x->parent->left = y;
        else
            x->parent->right = y;
        y->left = x;
        x->parent = y;
    }

    void rightRotate(RBNode<T>*& root, RBNode<T>* y) {
        RBNode<T>* x = y->left;
        y->left = x->right;
        if (x->right) x->right->parent = y;
        x->parent = y->parent;
        if (!y->parent)
            root = x;
        else if (y == y->parent->left)
            y->parent->left = x;
        else
            y->parent->right = x;
        x->right = y;
        y->parent = x;
    }

    void insertFixup(RBNode<T>*& root, RBNode<T>* z) {
        while (z->parent && z->parent->color == RED) {
            if (z->parent == z->parent->parent->left) {
                RBNode<T>* y = z->parent->parent->right;
                if (y && y->color == RED) {
                    z->parent->color = BLACK;
                    y->color = BLACK;
                    z->parent->parent->color = RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->right) {
                        z = z->parent;
                        leftRotate(root, z);
                    }
                    z->parent->color = BLACK;
                    z->parent->parent->color = RED;
                    rightRotate(root, z->parent->parent);
                }
            } else {
                RBNode<T>* y = z->parent->parent->left;
                if (y && y->color == RED) {
                    z->parent->color = BLACK;
                    y->color = BLACK;
                    z->parent->parent->color = RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->left) {
                        z = z->parent;
                        rightRotate(root, z);
                    }
                    z->parent->color = BLACK;
                    z->parent->parent->color = RED;
                    leftRotate(root, z->parent->parent);
                }
            }
        }
        root->color = BLACK;
    }

    void inorderHelper(RBNode<T>* node) const {
        if (!node) return;
        inorderHelper(node->left);
        std::cout << node->data << " ";
        inorderHelper(node->right);
    }

    RBNode<T>* searchHelper(RBNode<T>* node, T key) const {
        if (!node || node->data == key) return node;
        if (key < node->data) return searchHelper(node->left, key);
        else return searchHelper(node->right, key);
    }

public:
    RBTree() : root(nullptr) {}

    void insert(T key) {
        RBNode<T>* z = new RBNode<T>(key);
        RBNode<T>* y = nullptr;
        RBNode<T>* x = root;
        while (x) {
            y = x;
            if (z->data < x->data)
                x = x->left;
            else
                x = x->right;
        }
        z->parent = y;
        if (!y)
            root = z;
        else if (z->data < y->data)
            y->left = z;
        else
            y->right = z;
        insertFixup(root, z);
    }

    bool search(T key) const {
        return searchHelper(root, key) != nullptr;
    }

    void inorder() const {
        inorderHelper(root);
        std::cout << std::endl;
    }
};