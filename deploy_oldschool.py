{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "isInteractiveWindowMessageCell": true
   },
   "source": [
    "Connected to Python 3.11.4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Du står midt i en juratidsskog, og plutselig ser du en sulten dinosaur!\n",
      "Hva vil du gjøre?\n",
      "1. Løp for livet!\n",
      "2. Prøv å gjemme deg.\n",
      "Du prøver å gjemme deg bak et tre. Dinosauren ser deg ikke og går forbi. Du overlever!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "\n",
    "def intro():\n",
    "    print(\"Du står midt i en juratidsskog, og plutselig ser du en sulten dinosaur!\")\n",
    "\n",
    "def choose_action():\n",
    "    print(\"Hva vil du gjøre?\")\n",
    "    print(\"1. Løp for livet!\")\n",
    "    print(\"2. Prøv å gjemme deg.\")\n",
    "    return input(\"Skriv inn valg (1 eller 2): \")\n",
    "\n",
    "def result(action):\n",
    "    if action == \"1\":\n",
    "        print(\"Du løper så fort du kan, men dinosauren er raskere. Du blir spist opp!\")\n",
    "    elif action == \"2\":\n",
    "        print(\"Du prøver å gjemme deg bak et tre. Dinosauren ser deg ikke og går forbi. Du overlever!\")\n",
    "\n",
    "def play_dinosaur_game():\n",
    "    intro()\n",
    "    time.sleep(1)\n",
    "    action = choose_action()\n",
    "    result(action)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    play_dinosaur_game()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Du står midt i en juratidsskog, og plutselig ser du en sulten dinosaur!\n",
      "Hva vil du gjøre?\n",
      "1. Løp for livet!\n",
      "2. Prøv å gjemme deg.\n",
      "Du prøver å gjemme deg bak et tre. Dinosauren ser deg ikke og går forbi. Du overlever!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "\n",
    "def intro():\n",
    "    print(\"Du står midt i en juratidsskog, og plutselig ser du en sulten dinosaur!\")\n",
    "\n",
    "def choose_action():\n",
    "    print(\"Hva vil du gjøre?\")\n",
    "    print(\"1. Løp for livet!\")\n",
    "    print(\"2. Prøv å gjemme deg.\")\n",
    "    return input(\"Skriv inn valg (1 eller 2): \")\n",
    "\n",
    "def result(action):\n",
    "    if action == \"1\":\n",
    "        print(\"Du løper så fort du kan, men dinosauren er raskere. Du blir spist opp!\")\n",
    "    elif action == \"2\":\n",
    "        print(\"Du prøver å gjemme deg bak et tre. Dinosauren ser deg ikke og går forbi. Du overlever!\")\n",
    "\n",
    "def play_dinosaur_game():\n",
    "    intro()\n",
    "    time.sleep(1)\n",
    "    action = choose_action()\n",
    "    result(action)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    play_dinosaur_game()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
