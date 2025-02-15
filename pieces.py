import pygame

SQUARE_SIZE = 80  # Ensure SQUARE_SIZE is defined

# Load piece images
wP = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/whitePawn.png"), (SQUARE_SIZE, SQUARE_SIZE))
bP = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/blackPawn.png"), (SQUARE_SIZE, SQUARE_SIZE))

wR = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/whiteRook.png"), (SQUARE_SIZE, SQUARE_SIZE))
bR = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/blackRook.png"), (SQUARE_SIZE, SQUARE_SIZE))

wKnight = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/whiteKnight.png"), (SQUARE_SIZE, SQUARE_SIZE))
bKnight = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/blackKnight.png"), (SQUARE_SIZE, SQUARE_SIZE))

wB = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/whiteBishop.png"), (SQUARE_SIZE, SQUARE_SIZE))
bB = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/blackBishop.png"), (SQUARE_SIZE, SQUARE_SIZE))

wQ = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/whiteQueen.png"), (SQUARE_SIZE, SQUARE_SIZE))
bQ = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/blackQueen.png"), (SQUARE_SIZE, SQUARE_SIZE))

wK = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/whiteKing.png"), (SQUARE_SIZE, SQUARE_SIZE))
bK = pygame.transform.scale(pygame.image.load("/Users/ali/Desktop/pythonchess/images/blackKing.png"), (SQUARE_SIZE, SQUARE_SIZE))
