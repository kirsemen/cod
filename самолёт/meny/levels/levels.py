from самолёт.meny.levels.class_ import *
import pygame
from самолёт.config import *

levels = [Level([Block([300, 150]), Block([300, 50])], [Enemy_1([150, 150]), Enemy_2([200, 200])], 800),
          Level([Block([100, 100]), Block([200, 250])], [Enemy_1([100, 100]), Enemy_2([250, 250])], 500)]


def get_all_levels():
    return levels


def start_level(i, xp):
    level = levels[i]

    level.reload()
    level.player.xp = xp
    pygame.init()
    m_1 = 0
    pygame.display.set_caption("самолёт")

    clock = pygame.time.Clock()
    _stop = False
    surf = pygame.image.load("img/sky/2.png")
    surf = pygame.transform.scale(surf, size)
    while not _stop:
        _screen = pygame.display.set_mode(size)
        _screen.fill((30, 30, 30))
        _screen.blit(surf, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if debug:
                    print(level)
                _stop = True
            if debug:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    keys = pygame.key.get_pressed()
                    if event.button == 4:
                        m_1 += 30
                    elif event.button == 5:
                        m_1 -= 30
                    elif event.button == 1 and keys[pygame.K_1]:
                        pos = pygame.mouse.get_pos()
                        size_1 = Block([0, 0]).size
                        level.blocks.append(Block([pos[0] - size_1[0] / 2, pos[1] - size_1[1] / 2 - m_1]))
                    elif event.button == 1 and keys[pygame.K_2]:
                        pos = pygame.mouse.get_pos()
                        size_1 = Enemy_1([0, 0]).size
                        level.enemies.append(Enemy_1([pos[0] - size_1[0] / 2, pos[1] - size_1[1] / 2 - m_1]))
                    elif event.button == 1 and keys[pygame.K_3]:
                        pos = pygame.mouse.get_pos()

                        size_1 = Enemy_2([0, 0]).size
                        level.enemies.append(Enemy_2([pos[0] - size_1[0] / 2, pos[1] - size_1[1] / 2 - m_1]))

            else:
                click = level.handle_event(event)

                if click == "go to menu":
                    print(level.start_blocks)
                    return "go to menu", level.player.xp
                elif click == "next level":
                    return "next level", level.player.xp
                elif click == "restart":
                    return "restart", level.player.xp
                elif click == "go to menu, you win":
                    return "go to menu, you win", level.player.xp

        level.update()
        _screen = level.draw(_screen, m_1)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    return None, None
