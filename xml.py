from core.partida import *
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

def formata_saida(elem):
    		rough_string = ElementTree.tostring(elem, 'utf-8')
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(indent = " ")

funcionarios = Element('Ludo')
comment = Comment('Dados de Partida')
funcionarios.append(comment)

funcionario = SubElement(funcionarios, 'jogador')
nome = SubElement(funcionario, 'coordenadas')

nome_arquivo = 'partida.xml'
with open(nome_arquivo, 'w') as file_object:
		file_object.write(formata_saida(funcionarios))