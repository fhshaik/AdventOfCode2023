import System.IO
import Data.Text.Read (decimal)
import Data.Maybe (mapMaybe)
import Data.Text (Text, unpack)
import Text.Read (readMaybe)
import qualified Data.Text.Read as TR
import Data.Coerce (coerce)

import qualified Data.Text as T

add x y =  x + y

fwdDiff f n = f (n+1) - f n

numbersList :: [Int]
numbersList = [10,13,16,21,30,45,68]

square x = x * x


getNthElement :: [Int] -> Int -> Int
getNthElement list n
  | n >= 0 && n < length list = list !! n
  | otherwise = error "index out of bounds"


fallingFactorial k n
    | k < 0     = error "k must be a non-negative integer"
    | k == 0    = 1
    | otherwise = n * fallingFactorial (k - 1) (n - 1) 

factorial 0 = 1
factorial n = n * factorial (n - 1)

umbralTaylorSeries :: Int -> (Int -> Int) -> Int -> Int -> Double
umbralTaylorSeries n f x l
  | n>=l= 0
  | otherwise = (fromIntegral (composeNTimes n fwdDiff f 0) / fromIntegral (factorial n)) * fromIntegral (fallingFactorial n x) + umbralTaylorSeries (n + 1) f x l

composeNTimes n f x 
  | n==0 = x
  |otherwise = foldr1 (.) (replicate n f) x

splitEach :: T.Text -> [T.Text] -> [[T.Text]]
splitEach delimiter = map (T.splitOn delimiter)
textListToIntList :: [[Text]] -> [[Int]]
textListToIntList = map (map (read . T.unpack))


nextNumber :: [Int] -> Int
nextNumber var = round $ umbralTaylorSeries 0  (getNthElement var) (length var) (length var)

main = do
  contents <- readFile "C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input"
  let lst = lines contents
  let resultList = map (T.splitOn (T.pack " ")) (map T.pack lst)
  let intList = textListToIntList resultList
  let totalSum=sum(map nextNumber intList)
  print totalSum
