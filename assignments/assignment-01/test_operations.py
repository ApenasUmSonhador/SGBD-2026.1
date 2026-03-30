import pytest
from isam import ISAM


@pytest.fixture
def isam_tree():
    """Fixture para inicializar a árvore ISAM"""
    return ISAM('tree_configure.json')


class TestISAMOperations:
    """Testa as operações insert, search e remove da estrutura ISAM"""

    def test_insert(self, isam_tree):
        """Teste de inserção"""
        new_keys = [18, 22, 27, 35, 41, 44, 63, 67, 83, 86, 121, 145]
        for key in new_keys:
            isam_tree.insert(key)
        # Verify all keys were inserted
        for key in new_keys:
            assert isam_tree.search(key)

    def test_remove(self, isam_tree):
        """Teste de remoção"""
        # Insert keys first
        new_keys = [18, 22, 35, 41, 44, 63, 67, 83, 86, 121, 145]
        for key in new_keys:
            isam_tree.insert(key)
        
        # Remove keys
        keys_to_remove = [44, 67, 83, 145]
        for key in keys_to_remove:
            result = isam_tree.remove(key)
            assert result
        
        # Verify keys were removed
        for key in keys_to_remove:
            assert not isam_tree.search(key)

    def test_search_equality(self, isam_tree):
        """Teste de busca por igualdade"""
        new_keys = [18, 22, 27, 35, 41, 44, 63, 67, 83, 86, 121, 145]
        for key in new_keys:
            isam_tree.insert(key)
        
        # Test existing keys
        assert isam_tree.search(22)
        assert isam_tree.search(35)
        
        # Test non-existing key
        assert not isam_tree.search(90)

    def test_range_search(self, isam_tree):
        """Teste de busca por intervalo"""
        new_keys = [18, 22, 27, 35, 41, 44, 63, 67, 83, 86, 121, 145]
        for key in new_keys:
            isam_tree.insert(key)
        
        result_1 = isam_tree.range_search(20, 50)
        assert len(result_1) > 0
        
        result_2 = isam_tree.range_search(60, 90)
        assert len(result_2) > 0
        
        result_3 = isam_tree.range_search(120, 150)
        assert len(result_3) > 0
