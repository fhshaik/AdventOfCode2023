import System.IO
import Data.Text (Text, unpack)
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


fallingFactorial :: Int -> Int -> Int
fallingFactorial k n
  | k < 0     = error "k must be a non-negative integer"
  | k == 0    = 1
  | otherwise = product [n, n - 1..n - k + 1]

factorial :: Int -> Int
factorial n = product [1..n]

umbralTaylorSeries :: Int -> (Int -> Int) -> Int -> Int -> Double
umbralTaylorSeries n f x l
  | n >= l    = 0
  | otherwise = term + umbralTaylorSeries (n + 1) f x l
  where
    term = (fromIntegral (composeNTimes n fwdDiff f 0) / fromIntegral (factorial n)) * fromIntegral (fallingFactorial n x)

composeNTimes :: Int -> (a -> a) -> a -> a
composeNTimes n f x
  | n == 0    = x
  | otherwise = foldr1 (.) (replicate n f) x

splitEach :: T.Text -> [T.Text] -> [[T.Text]]
splitEach delimiter = map (T.splitOn delimiter)
textListToIntList :: [[Text]] -> [[Int]]
textListToIntList = map (map (read . T.unpack))


firstNumber :: [Int] -> Int
firstNumber var = round $ umbralTaylorSeries 0  (getNthElement var) (-1) (length var)

main = do
  contents <- readFile "C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input"
  let lst = lines contents
  let resultList = map (T.splitOn (T.pack " ")) (map T.pack lst)
  let intList = textListToIntList resultList
  --print (nextNumber [10,13,27,64,140,281,549,1101,2294,4858,10201,21027,42709,86382,175728,361360,750462,1566611,3268603,6783010,13951998])
  let totalSum=sum(map firstNumber intList)
  print totalSum
  let result = round $ umbralTaylorSeries 0  (getNthElement numbersList) 7 (length numbersList)
  print result
